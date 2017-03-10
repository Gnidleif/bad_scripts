#!/usr/bin/env python3
import json, re, os
from random import randint

def randomWord(words):
    return words[randint(0, len(words)-1)]

def randomPhrase(phrases):
    return phrases[randint(0, len(phrases)-1)]

def madLibPhrase(phrase, words):
    rgx = re.compile(r'(NOUN|ADJECTIVE|VERB)')

    m = re.search(rgx, phrase)
    while m is not None:
        head, body, tail = phrase[:m.span()[0]], phrase[m.span()[0]:m.span()[1]], phrase[m.span()[1]:]
        phrase = "".join([head, randomWord(words[body]), tail])
        m = re.search(rgx, phrase)
    return phrase

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

    amount = 1
    if args[0]:
        amount = int(args[0])

    result = []
    for i in range(amount+1):
        result.append(madLibPhrase(randomPhrase(phrases), words))
    print(" ".join(result))

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
