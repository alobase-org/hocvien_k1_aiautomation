#!/usr/bin/env python3
"""Build Remotion caption JSON from word timestamps and exact caption segments."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata


def token(value: str) -> str:
    value = unicodedata.normalize("NFC", value).casefold()
    return re.sub(r"[^0-9a-zà-ỹđ]+", "", value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--words", required=True)
    parser.add_argument("--segments", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--offset-ms", type=int, default=0)
    args = parser.parse_args()
    with open(args.words, encoding="utf-8") as handle:
        raw_words = json.load(handle)
    with open(args.segments, encoding="utf-8") as handle:
        segments = json.load(handle)
    if isinstance(raw_words, dict):
        raw_words = raw_words.get("words")
    if not isinstance(raw_words, list):
        raise SystemExit("words input must be a list or an object containing a 'words' list")
    if not isinstance(segments, list) or not all(isinstance(item, str) for item in segments):
        raise SystemExit("segments input must be a JSON array of strings")
    words = [w for w in raw_words if token(str(w.get("word", ""))) not in ("", "start", "end")]
    cursor = 0
    output = []
    for segment_index, text in enumerate(segments):
        expected = [token(x) for x in re.findall(r"\S+", text) if token(x)]
        actual = [token(str(w["word"])) for w in words[cursor:cursor + len(expected)]]
        if expected != actual:
            raise SystemExit(
                f"segment {segment_index} mismatch at word {cursor}: expected {expected}, got {actual}"
            )
        selected = words[cursor:cursor + len(expected)]
        start_ms = round(float(selected[0]["start"]) * 1000) + args.offset_ms
        end_ms = round(float(selected[-1]["end"]) * 1000) + args.offset_ms
        output.append({
            "text": text, "startMs": max(0, start_ms - 40), "endMs": end_ms + 120,
            "timestampMs": None, "confidence": None,
        })
        cursor += len(expected)
    if cursor != len(words):
        raise SystemExit(f"unused timestamp words: {len(words) - cursor}")
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(args.output)


if __name__ == "__main__":
    main()
