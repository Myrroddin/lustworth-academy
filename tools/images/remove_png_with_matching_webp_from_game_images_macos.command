#!/bin/bash

set -eu

dry_run=0
game_root=""

while [ "$#" -gt 0 ]; do
    case "$1" in
        --dry-run)
            dry_run=1
            ;;
        --game-root)
            shift
            if [ "$#" -eq 0 ]; then
                echo "Usage: $(basename "$0") [--dry-run] [--game-root <path-to-game>]" >&2
                exit 1
            fi
            game_root="$1"
            ;;
        *)
            echo "Usage: $(basename "$0") [--dry-run] [--game-root <path-to-game>]" >&2
            exit 1
            ;;
    esac

    shift
done

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

set --

if [ "$dry_run" -eq 1 ]; then
    set -- "$@" "--dry-run"
fi

if [ -n "$game_root" ]; then
    set -- "$@" "--game-root" "$game_root"
fi

exec "$python_cmd" "$python_script" "$@"
