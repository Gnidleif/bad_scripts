#!/usr/bin/env python3
import json, re, os
from random import randint

def chooseWord(words):
    return True

def run(args):
    if args is None:
        print("usage: {} <sentence amount>".format(__file__))
        exit(1337)
    if type(args) is not list:
        args = [args]

    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "words.json"), 'r') as f:
        words = json.load(f)

    with open(path.replace(scr_name, "phrases.txt"), 'r') as f:
        phrases = f.read().split('\n')

    for mood in words:
        for cls in words[mood]:
            for word in words[mood][cls]:
                print(word)

    for phrase in phrases:
        print(phrase)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
