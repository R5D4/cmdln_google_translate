"""
Translate a batch of files.

Usage:
    python gtrans ru en -i inputDir -o outputDir
"""

import argparse
import goslate

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Translate a batch of files.")
    parser.add_argument("from_lang", help="input language")
    parser.add_argument("to_lang", help="output language")
    parser.add_argument("-i", help="input directory")
    parser.add_argument("-o", help="output directory")
    parser.add_argument("-v", "--verbosity", action="count", help="verbosity")
    args = parser.parse_args()
    print args
