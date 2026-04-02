#!/bin/bash

set -eu

if [ "${1-}" = "--dry-run" ]; then
    set -- "--dry-run"
elif [ "$#" -ne 0 ]; then
    echo "Usage: $(basename "$0") [--dry-run]" >&2
    exit 1
fi

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
python_script="$script_dir/remove_png_with_matching_webp_from_game_images.py"

if [ ! -f "$python_script" ]; then
    echo "Python cleanup script not found: $python_script" >&2
    exit 1
fi

if command -v python3 >/dev/null 2>&1; then
    python_cmd="python3"
elif command -v python >/dev/null 2>&1; then
    python_cmd="python"
else
    echo "Python 3 was not found in PATH. Install Python 3 to run this tool." >&2
    exit 1
fi

exec "$python_cmd" "$python_script" "$@"
