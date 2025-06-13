#!/bin/bash
# Copy all Python files from /home/mehrain/workspace/gh/mms to the original minescript directory

SRC="/home/mehrain/workspace/gh/mms/minescript"
DST="/mnt/c/Users/Mehrain/curseforge/minecraft/Instances/Script Kid/minescript"

find "$SRC" -type f -name '*.py' -exec cp --parents {} "$DST" \;

echo "Python files copied from $SRC to $DST"
