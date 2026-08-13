#!/usr/bin/env bash
set -euo pipefail

video=""
music=""
voice=""
output=""
duration="81"
voice_offset_ms="2000"
music_gain="1"
voice_gain="1"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --video) video="$2"; shift 2 ;;
    --music) music="$2"; shift 2 ;;
    --voice) voice="$2"; shift 2 ;;
    --output) output="$2"; shift 2 ;;
    --duration) duration="$2"; shift 2 ;;
    --voice-offset-ms) voice_offset_ms="$2"; shift 2 ;;
    --music-gain) music_gain="$2"; shift 2 ;;
    --voice-gain) voice_gain="$2"; shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done

for value in "$video" "$music" "$voice" "$output"; do
  [[ -n "$value" ]] || { echo "Missing required argument" >&2; exit 2; }
done

ffmpeg -y -hide_banner \
  -i "$video" -i "$music" -i "$voice" \
  -filter_complex "[1:a]volume=${music_gain},apad,atrim=0:${duration}[piano];[2:a]volume=${voice_gain},adelay=${voice_offset_ms}|${voice_offset_ms},apad,atrim=0:${duration},asplit=2[sidechain][dialogue];[piano][sidechain]sidechaincompress=threshold=0.055:ratio=1.8:attack=24:release=320[ducked];[ducked][dialogue]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-15.5:TP=-1:LRA=5,atrim=0:${duration}[master]" \
  -map 0:v:0 -map "[master]" \
  -c:v copy -c:a aac -b:a 320k -ar 48000 \
  -movflags +faststart "$output"
