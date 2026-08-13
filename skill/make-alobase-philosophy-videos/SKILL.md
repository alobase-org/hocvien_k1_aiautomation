---
name: make-alobase-philosophy-videos
description: Produce finished Vietnamese vertical philosophy-for-leadership videos in the Alobase style, including research, script, native Vietnamese narration, original piano, captions, Remotion/FFmpeg assembly, loudness QA, and final MP4 delivery.
version: 1.1.0
---

# Make Alobase Philosophy Videos

## Purpose

Create a complete Vietnamese short-form video that applies a philosophical idea to management or leadership in the style of Nguyễn Minh Cường / Alobase.

The job is not complete at script stage. A successful run must end with a verified MP4 that contains working Vietnamese narration, audible piano, readable subtitles, and validated video/audio streams.

## Default output

- Language: Vietnamese
- Orientation: vertical 9:16
- Master: 1080×1920
- Mobile: 720×1280
- Duration target: 75–85 seconds
- No talking head, no presenter, no avatar on screen unless explicitly requested
- Visual tone: dark premium, minimal, cinematic, intelligent, restrained
- End card: `ALObase | Thiết kế lại cách con người làm việc`

## Editorial rules

1. Research one philosophical thesis with direct relevance to management or leadership.
2. Prefer original texts, scholarly sources, university references, or reputable management publications.
3. Verify quotations. Never invent a quote.
4. Avoid repeating the same philosopher, management problem, or central metaphor within 30 days when previous outputs can be checked.
5. Use philosophy as a lens for a concrete managerial dilemma, not as decorative quotation.
6. Avoid unnecessarily difficult foreign pronunciation in narration. Foreign concepts may appear on-screen, but narrate a natural Vietnamese equivalent where possible.

## Script pattern

Aim for 8–10 beats:

1. Hook: a managerial paradox or uncomfortable truth.
2. Name the philosophical idea.
3. Explain it in plain Vietnamese.
4. Contrast knowledge/rules/data with judgment.
5. Give one management example.
6. Give a second human/organizational example.
7. Turn the idea into a leadership principle.
8. Close with one memorable sentence.

At normal delivery, write enough text to land inside 75–85 seconds after TTS. Do not force a too-short narration by stretching audio later.

## Voice pipeline — mandatory

### Priority

Use a genuinely Vietnamese voice, not merely a generic multilingual voice.

Preferred profile:

- male
- low / deep timbre
- calm, intelligent, authoritative
- Northern / Hanoi-neutral if available
- speaking speed approximately **1.10×** normal

### Current proven fallback

HeyGen public voice:

- Name: `Cuong`
- Language metadata: `Vietnamese`
- Gender: `male`
- Voice ID: `8af68d7ea38f4e7ca05cf46c3f7a590b`

Use this voice before generic multilingual voices when available.

### Speed rule

Default TTS speed: **1.10**.

Because 1.10× reduces duration, re-estimate the script after synthesis. If narration falls below 75 seconds, improve/expand the script or add natural rhetorical pauses and resynthesize. Do not time-stretch the final voice simply to hit duration.

### Pronunciation gate

Before synthesizing the full script, generate a 10–20 second test containing Vietnamese diacritics and difficult words from the final script, e.g.:

`lãnh đạo, dữ liệu, phán đoán, tổ chức, thấu hiểu, nguyên tắc, tương lai`.

Reject the voice if tones, vowels, or sentence rhythm sound wrong.

**Never use a generic `Multilingual` voice without passing this pronunciation test first.**

### Foreign-word rule

If a concept such as `phronesis` is likely to be mispronounced, show the foreign term visually but narrate the Vietnamese equivalent, e.g. `sự khôn ngoan thực hành`.

## TTS asset retrieval fallback

If the execution environment can generate TTS but cannot download the returned CDN URL directly:

1. Create a temporary GitHub Actions workflow in a writable repository.
2. `curl -fL` the exact generated TTS URL into a WAV file.
3. Upload the WAV with `actions/upload-artifact@v4`.
4. Download the workflow artifact through the GitHub connector.
5. Materialize/unzip it into the working directory.
6. Delete the temporary workflow immediately after successful retrieval.

This bridge is a fallback only. Do not leave temporary workflows behind.

## Piano — mandatory

The video must contain real, clearly audible piano music, not ambient hiss, pads, or near-silence.

Desired music:

- gentle solo piano
- sparse chord voicings and melodic notes
- contemplative, warm, philosophical
- no synth drone
- no noisy texture masquerading as music
- smooth fade-in and fade-out

The piano may be generated programmatically or sourced from an approved original/royalty-safe asset, but it must be clearly recognizable as piano.

## Audio mix targets

Use these as practical QA targets, not cosmetic metadata:

- Narration: approximately **-16 LUFS integrated**
- Piano: approximately **8–12 dB below narration** during speech
- Master: roughly **-14 to -16 LUFS integrated**
- True peak: **≤ -1 dBTP**
- Stereo, 48 kHz
- No clipping
- No long accidental silences

The piano must still be audible on laptop and phone speakers at ordinary listening volume.

Do not accept a mix merely because the piano track technically exists. The requirement is perceptual: the listener must hear it.

## Visual style

Default visual language:

- charcoal / near-black background
- warm white typography
- restrained gold accents
- slow camera motion or abstract movement
- cinematic management metaphors
- diagrams, data, architecture, organizational imagery, decisions, trade-offs
- no cheesy stock presenter shots
- no corporate talking heads
- no excessive kinetic typography

## Captions

Captions are mandatory.

- Use word/sentence timestamps from the final narration where possible.
- Max 2 lines on screen.
- Keep captions inside mobile safe area.
- Use large, clean Vietnamese-capable font.
- Avoid line breaks that separate tightly connected Vietnamese phrases.
- Burn captions into the delivery master and also provide `.srt` or caption JSON when possible.

## Assembly

Preferred assembly stack:

- Remotion for scene timing, typography, transitions, and composition
- FFmpeg for final audio mixing, loudness normalization, encoding, muxing, and QA

Render visuals without trusting the render step to prove audio correctness. Treat audio mastering as an explicit production stage.

## Required QA gates

A run is **not complete** until all gates pass.

### Gate 1 — narration

- Native-sounding Vietnamese pronunciation confirmed on a test segment.
- Full narration duration measured.
- No broken tones, English-accented Vietnamese, or mangled key terms.

### Gate 2 — music

- Piano is recognizable as piano.
- Piano is clearly audible under speech on normal laptop/phone playback.
- Piano is not masking narration.

### Gate 3 — captions

- Captions match final narration.
- Max 2 lines.
- No overflow beyond safe area.
- Spot-check at least 3 frames: early, middle, late.

### Gate 4 — media streams

Use `ffprobe` or equivalent to confirm:

- master video exists and file size is non-zero
- video codec: H.264
- resolution: 1080×1920
- audio codec: AAC
- stereo
- sample rate: 48 kHz
- duration in the expected range

### Gate 5 — loudness

Use FFmpeg loudness analysis (`loudnorm`, `ebur128`, or equivalent) to verify voice/master loudness and peak safety.

### Gate 6 — deliverability

Open or probe the final MP4 after muxing. Do not hand off a path that has not been verified to exist.

## Failure policy

Never say any of the following unless verified:

- `video is being generated`
- `render succeeded`
- `audio is good`
- `completed`

If an API quota, TTS failure, CDN failure, render error, or missing asset blocks completion, state the blocker plainly and deliver only the parts that actually exist.

Do not substitute a session link for a finished video.

## Deliverables

For a full run, deliver:

1. Topic / title
2. Thesis in 1–2 sentences
3. 3–5 research sources
4. Final Vietnamese script
5. HQ MP4 1080×1920
6. Mobile MP4 720×1280
7. Subtitle file
8. Editable project ZIP
9. Voice WAV
10. Final mixed audio WAV when practical

## Daily-task operating rule

For scheduled production, finish the assets and QA before the delivery deadline. If the system must choose between publishing early and doing audio QA, choose audio QA.

A file with bad Vietnamese pronunciation or inaudible piano is a failed product, even if the MP4 renders successfully.
