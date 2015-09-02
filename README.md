# Command Line Google Translate (for many files)

python command line tool to translate multiple files with Google translate

## Goal

Want to be able to feed directories of text files to the script and have it
save the translated versions in a directory.

## Description

Uses goslate by Zhuo Qiang for the heavylifting.

## Usage

```bash
python translate.py ru en -i inputDir -o outputDir 
```

to translate all `.out` files in `inputDir` from Russian to English and put the
translated files in `outputDir`.

Add the `-v` optional flag to output status for each file being processed.

## Issues

Only translates `.out` files.

## Planned Updates

1. Allow user to indicate any file type (multiple types too) as input
2. Support both directory and file(s) as input

## Maybe Features

1. Automatically detect source language
2. Automatically detect encoding
3. Support Bash 4's globstar globbing
