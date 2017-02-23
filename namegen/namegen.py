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
    for i in range(1, len(name)):
        c = vowels[randint(0, len(vowels) - 1)] if name[i] in vowels else chr(randint(0, 25) + 97)
        name = name[:i] + c + name[i + 1:]
    return name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <your name>".format(sys.argv[0]))
        exit(1337)

    print(generator(sys.argv[1:]))
