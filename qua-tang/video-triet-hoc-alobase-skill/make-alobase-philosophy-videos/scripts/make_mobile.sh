#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: make_mobile.sh input-master.mp4 output-mobile.mp4" >&2
  exit 2
fi

input="$1"
output="$2"
[[ -f "$input" ]] || { echo "input does not exist: $input" >&2; exit 2; }

ffmpeg -y -hide_banner -i "$input" \
  -map 0:v:0 -map 0:a:0 \
  -c:v libx264 -preset medium -crf 25 -maxrate 2800k -bufsize 5600k \
  -pix_fmt yuv420p -c:a copy -movflags +faststart "$output"

source_audio_hash="$(ffmpeg -v error -i "$input" -map 0:a:0 -c copy -f hash -hash sha256 -)"
mobile_audio_hash="$(ffmpeg -v error -i "$output" -map 0:a:0 -c copy -f hash -hash sha256 -)"
if [[ "$source_audio_hash" != "$mobile_audio_hash" ]]; then
  echo "audio hash mismatch after mobile encode" >&2
  exit 1
fi

echo "$output"
