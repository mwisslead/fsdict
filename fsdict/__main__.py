import sys
import logging

from fsdict import FSDict

def main(argv=None):
    logging.basicConfig(level=logging.DEBUG)
    filedict = FSDict(argv[1] if len(argv) > 1 else None)
    for subfile in filedict:
        print(filedict[subfile])

if __name__ == '__main__':
    retval = main(sys.argv)
