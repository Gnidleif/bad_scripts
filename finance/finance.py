#!/usr/bin/env python3
import os
from random import randint

def run(args):
    if type(args) is not list or len(args) < 3:
        print("usage: {} <to> <from> <amount>".format(__file__))
        exit(1337)
    if type(args) is not list:
        args = [args]

    omitted = args[:2]
    enc = "latin-1"
    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "list.txt"), 'r', encoding=enc) as f:
        unf = f.read().splitlines()
        words = []
        for word in unf:
            if word not in omitted:
                words.append(word)

    print(len(words))

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
