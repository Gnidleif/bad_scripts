#!/usr/bin/env python3
import json, re, os
from random import randint

CAPITALIZE_CH = 30
CAPS_CH = 50
SPACE_CH = 20

def roll(chance):
    return randint(0, 100) <= chance

def fix(key, list, rgx):
    if key not in list:
        return key

    for word in list[key]:
        vars = re.findall(rgx, word)
        if len(vars) > 0:
            return " ".join([fix(i, list, rgx) for i in vars])
        else:
            index = randint(-1, len(list[key]) - 1)
            if index < 0:
                return key
            else:
                return list[key][index]

def beautify(words, list):
    res = []
    regex_word = re.compile(r'{(\w+)}')
    regex_sym = re.compile(r'{(\W+)}')
    for split in words.split():
        word = [i.lower() for i in re.split(r'\W+', split) if i is not '']
        for i in range(len(word)):
            word[i] = fix(word[i], list, regex_word)
        word = "".join(word)

        if roll(CAPITALIZE_CH):
            word = word.upper() if roll(CAPS_CH) else word.capitalize()

        sym = [i for i in re.split(r'\w+', split, flags=re.I) if i is not '']
        if len(sym) > 0:
            for i in range(len(sym)):
                sym[i] = fix(sym[i], list, regex_sym)
            sym = "".join(sym)

            if roll(SPACE_CH):
                sym = " " + sym
        else:
            sym = "".join(sym)

        res.append(word + sym)

    return " ".join(res)
    
def run(args):
    if args is None:
        print("usage: {} <args...>".format(__file__))
        exit(1337)
    if type(args) is not list:
        args = [args]

    enc = "latin-1"
    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "wordlist.json"), 'r', encoding=enc) as f:
        words = json.load(f)

    with open(path.replace(scr_name, "split_words.json"), 'r', encoding=enc) as f:
        words.update(json.load(f))

    for cmd in args:
        try:
            with open(cmd, 'r') as f:
                data = f.read()
        except FileNotFoundError as e:
            data = cmd

        outfile = path.replace(scr_name, "out.txt")
        f = open(outfile, 'wb').close()
        for line in data.split('\n'):
            res = beautify(line, words)
            with open(outfile, 'ab') as f:
                f.write("{}\n".format(res).encode('utf-8'))
            print(res)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])