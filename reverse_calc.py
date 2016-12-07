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

class Chromosome:
    def __init__(self, bits=''):
        self.bits = bits
        self.fitness = 0.0
        
    def calcFitness(self, target):
        result = 0.0
        self.bitsToEquation()
        try:
            result = eval(self.equation)
        except:
            self.fitness = 0.0
            return
        
        self.fitness = 999.0 if result == target else 1 / abs(target - result)
        
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
            
        self.equation = ''.join(result)
        
    def mutate(self):
        temp = []
        for i in range(len(self.bits)):
            bit = self.bits[i]
            if uniform(0, 1) <= MUT_RATE:
                bit = '1' if bit == '0' else '0'
            temp.append(bit)
        self.bits = ''.join(temp)
        
def roulette(pop, totFitness):
    result = ''
    slice = uniform(0, totFitness)
    soFar = 0.0
    for chromo in pop:
        soFar += chromo.fitness
        if soFar >= slice:
            result = chromo
            break
            
    return result
    
def crossover(p1, p2):
    offspring = Chromosome(p1.bits)
    if uniform(0, 1) <= CROSSOVER:
        splice = randint(0, CHROMO_LEN - 1)
        offspring.bits = p1.bits[splice:] + p2.bits[:splice]
        
    return offspring
        
def findSolution(pop, target):
    generation = 0
    results = []
    found = False
    while not found:
        generation += 1
        totFitness = 0.0
        for chromo in pop:
            chromo.calcFitness(target)
            totFitness += chromo.fitness
            
        for chromo in pop:
            if chromo.fitness == 999.0:
                found = True
                if chromo.equation not in results:
                    results.append(chromo.equation)
                    
        children = []
        for i in range(POP_SIZE):
            (dad, mom) = (roulette(pop, totFitness), roulette(pop, totFitness))
            child = crossover(dad, mom)
            child.mutate()
            children.append(child)
            
        pop = children[:]
        
    return results, generation
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <number(s)>".format(sys.argv[0]))
    
    for num in sys.argv[1:]:
        try:
            target = float(num) if '.' in num else int(num)
        except Exception as e:
            print("Exception: {}".format(e))
            continue
    
        pop = [Chromosome(''.join([str(randint(0, 1)) for x in range(CHROMO_LEN)])) for x in range(POP_SIZE)]
        (result, gen) = findSolution(pop, target)
        print("Target: {}\nEquation(s): {}\nGenerations: {}\n~".format(target, result, gen))