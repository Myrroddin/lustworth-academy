#!/usr/bin/env bash

set -eu

dry_run=0

if [ "${1-}" = "--dry-run" ]; then
    dry_run=1
    shift
fi

if [ "$#" -ne 0 ]; then
    echo "Usage: $(basename "$0") [--dry-run]" >&2
    exit 1
fi

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(CDPATH= cd -- "$script_dir/.." && pwd)"
audio_root="$repo_root/game/audio"

if [ ! -d "$audio_root" ]; then
    echo "Audio folder not found: $audio_root" >&2
    exit 1
fi

tmp_file="$(mktemp)"
trap 'rm -f "$tmp_file"' EXIT HUP INT TERM

find "$audio_root" -type f -iname '*.mp3' > "$tmp_file"
mp3_count="$(wc -l < "$tmp_file" | tr -d '[:space:]')"

if [ "$mp3_count" -eq 0 ]; then
    echo "No MP3 files found under game/audio"
    exit 0
fi

while IFS= read -r file_path; do
    relative_path="${file_path#$repo_root/}"

    if [ "$dry_run" -eq 1 ]; then
        echo "Would delete: $relative_path"
        continue
    fi

    echo "Deleting: $relative_path"
    rm -- "$file_path"
done < "$tmp_file"

echo "Scanned: game/audio"
echo "Found MP3 files: $mp3_count"

if [ "$dry_run" -eq 1 ]; then
    echo "Dry run only. No files were deleted."
else
    echo "Deleted all MP3 files successfully."
fi