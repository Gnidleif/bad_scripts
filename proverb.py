#!/usr/bin/env python3
from random import randint

def makeProverb(data):
    (first, second) = [data[randint(0, len(data) - 1)].split(' ') for i in range(2)]
    head = " ".join(first[:int(len(first) / 2)])
    tail = " ".join(second[int(len(second) / 2):])

    return "{} {}".format(head, tail)

if __name__ == "__main__":
    with open("list_proverbs.txt") as f:
            data = f.read().splitlines()

    print(makeProverb(data))
