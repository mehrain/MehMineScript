#!/bin/bash
# Copy all Python files from SRC (top-level only) to DST (flat, no directory structure)

SRC="/home/mehrain/workspace/gh/mms/minescript"
DST="/mnt/c/Users/Mehrain/curseforge/minecraft/Instances/Script Kid/minescript"

find "$SRC" -maxdepth 1 -type f -name '*.py' -exec cp {} "$DST" \;

echo "Python files copied from $SRC to $DST"
