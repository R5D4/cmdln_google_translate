# Command Line Google Translate (for many files)

python command line tool to translate multiple files

## Goal

Want to be able to feed directories of text files to the script and have it
output the translated versions.

Something like:

```bash
./translate inputDir outputDir ru en
```

to translate all files in `inputDir` from Russian to English and put the
translated files in `outputDir`.

Might also allow regex to indicate what files to include, like:

```bash
./translate inputDir/*.py outputDir ru en
```

which will only translate the `.py` files.
