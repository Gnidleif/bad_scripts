#!/usr/bin/env python3
import json, re, os
from random import randint

def randomWord(words):
    return words[randint(0, len(words)-1)]

def randomPhrase(phrases):
    return phrases[randint(0, len(phrases)-1)]

def madLibPhrase(phrase, words):
    cls = re.compile(r'(NOUN|ADJECTIVE|VERB)') # Finds proper word class
    form = re.compile(r'(DEF|IND)_')
    end = re.compile(r'\|(en|et|t|n)$')
    rmv = re.compile(r'\|')
    m = re.search(cls, phrase)

    while m is not None:
        head, body, tail = phrase[:m.span()[0]], phrase[m.span()[0]:m.span()[1]], phrase[m.span()[1]:]
        word = randomWord(words[body])

        # Handle noun cases
        if m.group() == "NOUN":
            n = re.search(form, head)
            head = head[:-len(n.group())]
            if n.group() == "IND_":
                o = re.search(end, word)
                word = word[:-len(o.group())]

        if len(head) == 0:
            word = word.capitalize()
        phrase = "".join([head, re.sub(rmv, '', word), tail])
        m = re.search(cls, phrase)
        n = re.search(form, phrase)
    return phrase

def run(args):
    if type(args) is not list or len(args) < 1:
        print("usage: {} <personality> <amount>".format(__file__))
        exit(1337)

    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    if not os.path.isdir(path.replace(scr_name, args[0])):
        print("directory {} doesn't exist".format(args[0]))
        exit(1337)

    with open(path.replace(scr_name, "{}/words.json".format(args[0])), 'r') as f:
        words = json.load(f)

    with open(path.replace(scr_name, "{}/phrases.txt".format(args[0])), 'r') as f:
        phrases = f.read().splitlines()

    amount = 1
    if args[1]:
        amount = int(args[1])

    result = []
    for i in range(amount):
        result.append(madLibPhrase(randomPhrase(phrases), words))
    print(" ".join(result))

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
