#!/usr/bin/env python3
import sys
from random import randint, uniform

CHROMO_LEN = 100
MUT_RATE = 0.001
POP_SIZE = 10
GENE_LEN = 4
CROSSOVER = 0.7

nums = {
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
}

ops = {
    '1010': '+',
    '1011': '-',
    '1100': '*',
    '1101': '/',
}

class Chromo:
    def __init__(self, bits=""):
        self.bits = bits if bits is not "" else ''.join([str(randint(0, 1)) for x in range(CHROMO_LEN)])
        self.fitness = 0.0
        self.equation = ""
        
    def calcFitness(self, target):
        result = 0.0
        self.bitsToEquation()
        try:
            result = eval(self.equation)
        except:
            self.fitness = 0.0
            return
        
        self.fitness = 999.0 if result == target else 1 / abs(target - result)
        # Debugging
        print("Fitness: {}\nBits: {}\nResult: {} = {}\n=============".format(self.bits, self.equation, result, self.fitness))
        
    def bitsToEquation(self):
        result = []
        numTurn = True
        for i in range(0, len(self.bits), GENE_LEN):
            gene = self.bits[i:i+GENE_LEN]
            if numTurn:
                if gene in nums:
                    result.append(nums[gene])
                    numTurn = False
            else:
                if gene in ops:
                    result.append(ops[gene])
                    numTurn = True
        
        if result[-1] not in nums.values():
            result = result[:-1]
            
        self.equation = ''.join(result)
        
class Population:
    def __init__(self):
        self.chromos = [Chromo() for x in range(POP_SIZE)]
        self.totFitness = 0.0
        
def roulette(pop):
    slice = uniform(0, pop.totFitness)
    sofar = 0.0
    for chromo in pop.chromos:
        sofar += chromo.fitness
        if sofar >= slice:
            return chromo
    return ""
        
def findSolution(pop, target):
    results = []
    found = False
    while not found:
        for chromo in pop.chromos:
            chromo.calcFitness(target)
            pop.totFitness += chromo.fitness
            
        for chromo in pop.chromos:
            if chromo.fitness == 999.0:
                found = True
                if chromo.equation not in results:
                    results.append(chromo.equation)
                    
        children = Population()
                
        pop.totFitness = 0.0
        found = True
        
    # Should really return a set of valid strings
    return results
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <number(s)>".format(sys.argv[0]))
        sys.exit(1337)
    
    try:
        target = int(sys.argv[1])
    except Exception as e:
        print("Exception: {}".format(e))
        sys.exit(1337)
    
    result = findSolution(Population(), target)
    print(result)