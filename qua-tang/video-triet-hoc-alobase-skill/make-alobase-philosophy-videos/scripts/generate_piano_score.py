#!/usr/bin/env python3
"""Generate an original, sparse neo-classical piano score as 48 kHz stereo WAV."""

from __future__ import annotations

import argparse
import math
import os
import subprocess
import tempfile
import wave

import numpy as np


SR = 48_000


def midi_hz(note: int) -> float:
    return 440.0 * (2.0 ** ((note - 69) / 12.0))


def piano_note(freq: float, seconds: float, velocity: float, phase_seed: int) -> np.ndarray:
    count = max(1, int(seconds * SR))
    t = np.arange(count, dtype=np.float64) / SR
    result = np.zeros(count, dtype=np.float64)
    rng = np.random.default_rng(phase_seed)
    inharmonicity = 0.000045 * (max(freq, 55.0) / 440.0) ** 0.28
    brightness = 0.72 + 0.55 * velocity

    for partial in range(1, 13):
        stretched = partial * math.sqrt(1.0 + inharmonicity * partial * partial)
        partial_freq = freq * stretched
        if partial_freq >= SR * 0.46:
            break
        amplitude = (brightness ** (partial - 1)) / (partial ** 1.28)
        decay = (3.8 + 2.1 * (220.0 / max(freq, 70.0)) ** 0.35) / (1.0 + 0.24 * (partial - 1))
        phase = rng.uniform(-0.05, 0.05)
        result += amplitude * np.sin(2 * np.pi * partial_freq * t + phase) * np.exp(-t / decay)

    attack = np.minimum(1.0, t / 0.006)
    release_start = max(0.05, seconds - 0.38)
    release = np.ones_like(t)
    mask = t > release_start
    release[mask] = np.exp(-(t[mask] - release_start) / 0.20)
    hammer = (
        np.sin(2 * np.pi * freq * 7.03 * t)
        + 0.55 * np.sin(2 * np.pi * freq * 11.09 * t + 0.2)
    ) * np.exp(-t / 0.018)
    result = (result + 0.035 * hammer) * attack * release
    peak = max(1e-9, float(np.max(np.abs(result))))
    return result / peak * velocity


def add_note(audio: np.ndarray, start: float, note: int, duration: float, velocity: float, seed: int) -> None:
    data = piano_note(midi_hz(note), duration, velocity, seed)
    begin = int(start * SR)
    end = min(len(audio), begin + len(data))
    if end <= begin:
        return
    data = data[: end - begin]
    pan = np.clip((note - 60) / 38.0, -0.72, 0.72)
    left = math.sqrt((1.0 - pan) * 0.5)
    right = math.sqrt((1.0 + pan) * 0.5)
    audio[begin:end, 0] += data * left
    audio[begin:end, 1] += data * right


def add_room(audio: np.ndarray) -> np.ndarray:
    dry = audio.copy()
    wet = np.zeros_like(audio)
    taps = [
        (0.043, 0.105, -1), (0.071, 0.082, 1), (0.109, 0.061, -1),
        (0.163, 0.047, 1), (0.239, 0.035, -1), (0.347, 0.026, 1),
        (0.503, 0.018, -1), (0.719, 0.012, 1),
    ]
    for delay_s, gain, cross in taps:
        delay = int(delay_s * SR)
        if delay >= len(audio):
            continue
        if cross < 0:
            wet[delay:, 0] += dry[:-delay, 1] * gain
            wet[delay:, 1] += dry[:-delay, 0] * gain
        else:
            wet[delay:] += dry[:-delay] * gain
    return dry + wet


def compose(duration: float, bpm: float, seed: int) -> np.ndarray:
    audio = np.zeros((int(duration * SR), 2), dtype=np.float64)
    beat = 60.0 / bpm
    bar = beat * 4
    start = 0.55
    bars = int(math.ceil((duration - start) / bar))
    progression = [
        {"bass": (38, 45), "arp": (53, 57, 60, 64, 69)},
        {"bass": (34, 41), "arp": (50, 53, 57, 62, 65)},
        {"bass": (41, 48), "arp": (53, 57, 60, 67, 69)},
        {"bass": (36, 43), "arp": (50, 55, 60, 62, 67)},
    ]
    rng = np.random.default_rng(seed)
    seed_counter = seed * 1000

    for bar_index in range(bars):
        chord = progression[bar_index % len(progression)]
        bar_start = start + bar_index * bar
        if bar_start >= duration:
            break
        intro = bar_index < 3
        outro = bar_index >= bars - 4
        climax = int(bars * 0.60) <= bar_index < int(bars * 0.82)
        base_velocity = 0.22 if intro or outro else (0.33 if climax else 0.28)

        for beat_pos, bass_note in ((0.0, chord["bass"][0]), (2.0, chord["bass"][1])):
            jitter = rng.uniform(-0.018, 0.018)
            add_note(audio, bar_start + beat_pos * beat + jitter, bass_note, bar * 0.92,
                     base_velocity * (1.03 if beat_pos == 0 else 0.78), seed_counter)
            seed_counter += 1

        pattern = [0, 2, 1, 3, 2, 4, 1, 3]
        if bar_index % 4 == 3:
            pattern = [0, 2, 1, 3, 4, 3, 2, 1]
        step_count = 4 if intro else (5 if outro else 8)
        for step in range(step_count):
            pos = (step * 0.5 + (0.5 if intro else 0.0)) * beat
            note = chord["arp"][pattern[step]]
            if climax and step in (3, 7):
                note += 12
            jitter = rng.uniform(-0.026, 0.026)
            velocity = base_velocity * (0.72 + 0.18 * (step % 3))
            add_note(audio, bar_start + pos + jitter, note, beat * 2.15, velocity, seed_counter)
            seed_counter += 1

        if not intro and not outro and bar_index % 2 == 1:
            melody = chord["arp"][4] + (12 if climax else 0)
            add_note(audio, bar_start + 1.45 * beat, melody, beat * 2.7,
                     base_velocity * 0.82, seed_counter)
            seed_counter += 1

    audio = add_room(audio)
    fade_in = min(len(audio), int(1.8 * SR))
    fade_out = min(len(audio), int(3.5 * SR))
    audio[:fade_in] *= np.linspace(0.0, 1.0, fade_in)[:, None]
    audio[-fade_out:] *= np.linspace(1.0, 0.0, fade_out)[:, None]
    peak = max(1e-9, float(np.max(np.abs(audio))))
    return audio / peak * 0.66


def write_wav(path: str, audio: np.ndarray) -> None:
    pcm = np.clip(audio, -1.0, 1.0)
    pcm = (pcm * 32767.0).astype("<i2")
    with wave.open(path, "wb") as handle:
        handle.setnchannels(2)
        handle.setsampwidth(2)
        handle.setframerate(SR)
        handle.writeframes(pcm.tobytes())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--duration", type=float, default=81.0)
    parser.add_argument("--bpm", type=float, default=72.0)
    parser.add_argument("--seed", type=int, default=23)
    parser.add_argument("--target-lufs", type=float, default=-24.0)
    args = parser.parse_args()
    if args.duration <= 5 or not 45 <= args.bpm <= 100:
        raise SystemExit("duration must be >5 seconds and bpm must be 45–100")
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    audio = compose(args.duration, args.bpm, args.seed)
    with tempfile.TemporaryDirectory() as tmp:
        raw = os.path.join(tmp, "piano-raw.wav")
        write_wav(raw, audio)
        subprocess.run([
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", raw,
            "-af", f"loudnorm=I={args.target_lufs}:TP=-3:LRA=7",
            "-ar", str(SR), "-c:a", "pcm_s16le", args.output,
        ], check=True)
    print(args.output)


if __name__ == "__main__":
    main()
