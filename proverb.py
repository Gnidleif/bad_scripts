#!/usr/bin/env python3
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

if __name__ == "__main__":
    with open("list_proverbs.txt") as f:
            data = f.read().splitlines()

    print(makeProverb(data))
