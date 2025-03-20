#!/bin/bash

USERFILE="users.txt"

if [ ! -f "$USERFILE" ]; then
    echo "File '$USERFILE' not found!"
    exit 1
fi

while read -r user; do
    sudo useradd "$user"
    echo "User '$user' added."
done < "$USERFILE"