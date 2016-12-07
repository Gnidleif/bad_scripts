#!/usr/bin/env python3
import sys
from random import randint

vowels = ['aoueiy']

def nameGen(name):
    for c in name[1:]:
        c = chr(randint(0, 25) + 97)
        print(c)
   return name

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <your name>".format(sys.argv[0]))
        sys.exit(1337)

    names = ' '.join(sys.argv[1:]).split(' ') # Pure beauty
    for i in range(len(names)):
        names[i] = nameGen(names[i])
    print(' '.join(names))
