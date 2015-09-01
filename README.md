# Command Line Google Translate (for many files)

python command line tool to translate multiple files

## Goal

Want to be able to feed directories of text files to the script and have it
output the translated versions.

## Description

Uses goslate by Zhuo Qiang for the heavylifting.

## Usage

```bash
python translate.py ru en -i inputDir -o outputDir 
```

to translate all files in `inputDir` from Russian to English and put the
translated files in `outputDir`.

In the future, might allow regex to indicate what files to include, like:

```bash
python translate.py ru en -i inputDir/*.py -o outputDir
```

which will only translate the `.py` files.

## Issues

Behavior using relational paths isn't robust.

e.g. passing `../inputDir` or `../outputDir` has undesirable results.

Script works when used from one directory level above input and output
directories.

## Planned Updates

1. Fix relative path issue
2. Upgrade to support regex to indicate input files (maybe)
3. Automatically detect encoding
4. Automatically detect source language (maybe)
