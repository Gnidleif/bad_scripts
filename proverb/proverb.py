#!/usr/bin/env python3
import os
from random import randint

def randomize(data):
    (a, b) = [randint(0, len(data) - 1) for i in range(2)]
    while a == b:
        b = randint(0, len(data) - 1)
    return data[a].split(' '), data[b].split(' ')

def makeProverb(data):
    (first, second) = randomize(data)
    head = " ".join(first[:int(len(first) / 2) + 1])
    tail = " ".join(second[int(len(second) / 2):])

    return "{} {}".format(head, tail)
    
def run(args):
    if args is None:
        print("usage: {} <amount>".format(__file__))
        exit(1337)
    if type(args) is not list:
        args = [args]
        
    amount = int(args[0])
    path = os.path.abspath(__file__)
    scr_name = os.path.basename(__file__)
    with open(path.replace(scr_name, "list_proverbs.txt"), 'r') as f:
        data = f.read().splitlines()
    
    for i in range(amount):
        print("{}: {}".format(i + 1, makeProverb(data)))
        
if __name__ == "__main__":
    import sys
    run(sys.argv[1:])

