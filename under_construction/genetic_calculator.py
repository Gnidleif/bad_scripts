#!/usr/bin/env python3
import sys
from random import randint

# Classes
class Population:
    def __init__(self, pop_size, chromo_len):
        self.chromos = [Chromo(chromo_len) for x in range(pop_size)]

class Chromo:
    def __init__(self, chromo_len, fitness=0.0):
        self.bits = ''.join([str(randint(0, 1)) for x in range(chromo_len)])
        self.fitness = fitness

# Constants
chromo_len = 100
mut_rate = 0.001
pop_size = 10
gene_len = 4
cross = 0.7
genes = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': '+',
    '1011': '-',
    '1100': '*',
    '1101': '/'
}

# Functions
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <number(s)>".format(sys.argv[0]))
        sys.exit(1337)
    
    try:
        target = int(sys.argv[1])
    except Exception as e:
        print("Exception: {}".format(e))
        sys.exit(1337)
    
    found = False
    pop = Population(pop_size, chromo_len)
    