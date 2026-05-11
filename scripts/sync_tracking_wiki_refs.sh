#!/bin/zsh

set -euo pipefail
setopt null_glob

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_WIKI_ROOT="${1:-/Users/zyhjr/Desktop/source/llm-wiki-skill/tracking-wiki}"
TARGET_ROOT="${2:-$SKILL_ROOT/references/prod/tracking-wiki}"

if [[ ! -f "$SOURCE_WIKI_ROOT/wiki/index.md" ]]; then
  echo "Missing source wiki index: $SOURCE_WIKI_ROOT/wiki/index.md" >&2
  exit 1
fi

if [[ ! -f "$SOURCE_WIKI_ROOT/raw/tracking/overview.md" ]]; then
  echo "Missing snapshot overview: $SOURCE_WIKI_ROOT/raw/tracking/overview.md" >&2
  exit 1
fi

if [[ ! -f "$SOURCE_WIKI_ROOT/raw/tracking/export-metadata.json" ]]; then
  echo "Missing export metadata: $SOURCE_WIKI_ROOT/raw/tracking/export-metadata.json" >&2
  exit 1
fi

mkdir -p "$TARGET_ROOT/raw/tracking"

rm -rf "$TARGET_ROOT/concepts"
rm -rf "$TARGET_ROOT/entities"
rm -rf "$TARGET_ROOT/summaries"
rm -rf "$TARGET_ROOT/raw/tracking"
rm -f "$TARGET_ROOT/index.md"

cp -R "$SOURCE_WIKI_ROOT/wiki/." "$TARGET_ROOT/"
mkdir -p "$TARGET_ROOT/raw/tracking"
cp "$SOURCE_WIKI_ROOT/raw/tracking/overview.md" "$TARGET_ROOT/raw/tracking/overview.md"
cp "$SOURCE_WIKI_ROOT/raw/tracking/export-metadata.json" "$TARGET_ROOT/raw/tracking/export-metadata.json"

echo "Synced tracking wiki references to $TARGET_ROOT"
