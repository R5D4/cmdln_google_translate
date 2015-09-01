"""
Translate a batch of files.

Usage:
    python gtrans ru en -i inputDir -o outputDir -v 
"""

import concurrent.futures
import os
import errno
import argparse
import goslate

# only translate *.out
OUT_EXT = 'out'
# instantiate a Goslate object for the entire script
GS = goslate.Goslate()


def make_dir(path):
    """ Try to create the output directory."""
    try:
        os.makedirs(path)
    except OSError as exception:
        # if directory already exists do nothing
        if exception.errno != errno.EEXIST:
            raise


def translate_file(from_lang, to_lang, in_file, out_dir, verbose):
    if verbose:
        print "Translating %s... " % in_file,

    translated_lines = GS.translate(open(in_file), to_lang, from_lang)
    translation = '\n'.join(translated_lines)
    # determine output file name and directory
    # remove the .out so we can add the new extension
    file_base, ext = os.path.splitext(in_file)
    out_file = os.path.join(out_dir, file_base+'.'+to_lang)
    make_dir(os.path.dirname(out_file))
    
    with open(out_file, 'w') as output:
        print translation
        output.write(translation)

    if verbose:
        print "Done."

def translate_dir(from_lang, to_lang, in_dir, out_dir, verbose):
    for root, dirs, files in os.walk(in_dir):
        for f in files:
            file_name, file_ext = os.path.splitext(f)
            # translate *.out
            if file_ext == '.'+OUT_EXT:
                in_file = os.path.join(root, f)
                translate_file(from_lang, to_lang, in_file, out_dir, verbose)
            else:
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Translate a batch of files.")
    parser.add_argument("from_lang", help="input language")
    parser.add_argument("to_lang", help="output language")
    parser.add_argument("-i", help="input directory")
    parser.add_argument("-o", help="output directory")
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="verbosity")
    args = parser.parse_args()
    print args

    if not (args.i and args.o):
        print "Please indicate input and output directories."
    elif args.verbose:
        print "Will output path and name of each file."
        translate_dir(args.from_lang, args.to_lang, args.i, args.o, 
                      args.verbose)
    elif not args.verbose:
        print "Translating files in {} from {} to {}... ".format(args.i,
                                                                args.from_lang,
                                                                args.to_lang),
        translate_dir(args.from_lang, args.to_lang, args.i, args.o) 
        print "Done."
