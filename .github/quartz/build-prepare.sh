#!/usr/bin/env bash
set -e

NOTES_DIR="$1"
QUARTZ_DIR="$2"

if [ -z "$NOTES_DIR" ] || [ -z "$QUARTZ_DIR" ]; then
    echo "Error: Missing arguments. Usage: bash build-prepare.sh <notes-dir> <quartz-dir>"
    exit 1
fi

echo "Step 1/5: Cleaning old content..."
rm -rf "$QUARTZ_DIR/content/"*

echo "Step 2/5: Applying hash patch..."
git -C "$QUARTZ_DIR" checkout quartz/util/path.ts 2>/dev/null || true
git -C "$QUARTZ_DIR" apply "$NOTES_DIR/.github/quartz/hash-urls.patch"

echo "Step 3/5: Copying configs and styles..."
cp "$NOTES_DIR/.github/quartz/"*.ts "$QUARTZ_DIR/"
if [ -f "$NOTES_DIR/.github/quartz/custom.scss" ]; then
    git -C "$QUARTZ_DIR" checkout quartz/styles/custom.scss 2>/dev/null || true
    echo "" >> "$QUARTZ_DIR/quartz/styles/custom.scss"
    cat "$NOTES_DIR/.github/quartz/custom.scss" >> "$QUARTZ_DIR/quartz/styles/custom.scss"
fi

echo "Step 4/5: Copying notes and meta-files..."

find "$NOTES_DIR" -maxdepth 1 -type d -name "*семестр*" -exec cp -r {} "$QUARTZ_DIR/content/" \;

if [ -f "$NOTES_DIR/.index.md" ]; then
    cp "$NOTES_DIR/.index.md" "$QUARTZ_DIR/content/index.md"
else
    echo "Warning: .index.md not found in the root. Site homepage will be empty."
fi

if [ -f "$NOTES_DIR/README.md" ]; then
    cp "$NOTES_DIR/README.md" "$QUARTZ_DIR/content/readme.md"
fi

if [ -f "$NOTES_DIR/CONTRIBUTING.md" ]; then
    cp "$NOTES_DIR/CONTRIBUTING.md" "$QUARTZ_DIR/content/contributing.md"
fi

echo "Step 5/5: Generating index.md metadata..."
find "$QUARTZ_DIR/content" -mindepth 1 -type d | while read -r dir; do
    foldername=$(basename "$dir")
    index_file="$dir/index.md"

    if [ ! -f "$index_file" ]; then
        cat <<EOF > "$index_file"
---
title: "$foldername"
---
EOF
    fi
done

echo "Success: Preparation complete."
