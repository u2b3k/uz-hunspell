#!/bin/bash

filename="$1"
if [ -z "$filename" ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Check if the input file exists
if [ ! -f "$filename" ]; then
    echo "File not found: $filename"
    exit 1
fi

# Remove empty lines and duplicates, sort alphabetically
tail -n +2 "$filename" | grep -v '^$' | sort -u > sorted_words.txt

# Count lines
word_count=$(wc -l < sorted_words.txt)

# Combine word count and sorted entries
(echo $word_count; cat sorted_words.txt) > "$filename"

# Clean up temporary file
rm sorted_words.txt
echo "Sorted words written to $filename with $word_count entries."
