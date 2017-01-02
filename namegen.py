#!/usr/bin/env python3
import sys
from random import randint

vowels = "aoueiy"

def generator(names):
    names = ' '.join(names).split(' ')
    for i in range(len(names)):
        names[i] = nameGen(names[i])
    return ' '.join(names)

def nameGen(name):
    name = list(name)
    for i in range(1, len(name)):
        name[i] = vowels[randint(0, len(vowels) - 1)] if name[i] in vowels else chr(randint(0, 25) + 97)

    return str(''.join(name))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <your name>".format(sys.argv[0]))
        sys.exit(1337)

    names = generator(sys.argv[1:])
    print(names)
