import collections
from functools import lru_cache
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string")
parser.add_argument("-f", "--file")
args = parser.parse_args()

@lru_cache(maxsize=15)
def clearword(string):
    print(string)
    c = collections.Counter()
    for word in list(string):
        c[word] += 1
    print(len(c))
    return len(c)


if args.string and args.file ==None:
    clearword(args.string)
elif args.file:
    filename = args.file
    lines = Path(filename).read_text().splitlines()
    for word in lines:
        clearword(word)