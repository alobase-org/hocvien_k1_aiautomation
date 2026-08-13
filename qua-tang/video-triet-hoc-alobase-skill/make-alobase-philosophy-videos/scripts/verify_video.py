#!/usr/bin/env python3
"""Fail fast when a vertical philosophy-video deliverable misses technical QA."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import re
import subprocess
import sys


def run(*args: str) -> str:
    return subprocess.run(args, check=True, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT).stdout


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--min-duration", type=float, default=75.0)
    parser.add_argument("--max-duration", type=float, default=85.0)
    parser.add_argument("--min-lufs", type=float, default=-16.8)
    parser.add_argument("--max-lufs", type=float, default=-14.5)
    parser.add_argument("--max-true-peak", type=float, default=-0.8)
    args = parser.parse_args()
    probe = json.loads(run(
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration:stream=codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels",
        "-of", "json", args.video,
    ))
    duration = float(probe["format"]["duration"])
    video = next((s for s in probe["streams"] if s["codec_type"] == "video"), None)
    audio = next((s for s in probe["streams"] if s["codec_type"] == "audio"), None)
    errors = []
    if not video or (video.get("width"), video.get("height")) != (1080, 1920):
        errors.append("video must be 1080x1920")
    elif abs(float(Fraction(video.get("avg_frame_rate", "0/1"))) - 30.0) > 0.01:
        errors.append("video must be 30 fps")
    if not args.min_duration <= duration <= args.max_duration:
        errors.append(f"duration {duration:.3f}s is outside range")
    if not audio or audio.get("codec_name") != "aac" or int(audio.get("channels", 0)) != 2:
        errors.append("AAC stereo audio track is required")
    elif int(audio.get("sample_rate", 0)) != 48_000:
        errors.append("audio must be 48 kHz")
    if Path(args.video).suffix.casefold() == ".mp4":
        with open(args.video, "rb") as handle:
            header = handle.read(2_000_000)
        moov = header.find(b"moov")
        mdat = header.find(b"mdat")
        if moov < 0 or (mdat >= 0 and moov > mdat):
            errors.append("MP4 is missing faststart metadata")
    run("ffmpeg", "-v", "error", "-i", args.video, "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-")
    loud = run("ffmpeg", "-hide_banner", "-i", args.video, "-map", "0:a:0",
               "-af", "ebur128=peak=true:framelog=verbose", "-f", "null", "-")
    integrated = re.findall(r"I:\s+(-?\d+(?:\.\d+)?) LUFS", loud)
    peaks = re.findall(r"Peak:\s+(-?\d+(?:\.\d+)?) dBFS", loud)
    if not integrated or not peaks:
        errors.append("could not measure loudness")
    else:
        lufs = float(integrated[-1])
        peak = float(peaks[-1])
        if not args.min_lufs <= lufs <= args.max_lufs:
            errors.append(f"integrated loudness {lufs:.1f} LUFS is outside range")
        if peak > args.max_true_peak:
            errors.append(f"true peak {peak:.1f} dBFS is too high")
    silence = run("ffmpeg", "-hide_banner", "-i", args.video, "-map", "0:a:0",
                  "-af", "silencedetect=noise=-45dB:d=1.5", "-f", "null", "-")
    if "silence_duration:" in silence:
        errors.append("unexpected silence >=1.5s detected")
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    print(f"PASS: {duration:.3f}s, 1080x1920, AAC stereo, loudness and peak within limits")


if __name__ == "__main__":
    main()
