#!/usr/bin/env python3
from random import randint

keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]

def randChar(c):
    part = -1
    index = -1
    for i in range(len(keys)):
        if c in keys[i]:
            part = i
            index = keys[i].index(c)
            break
            
    if index is -1:
        return c
    
    flip = randint(-1, 1)
    if flip is 0:
        c = ''
    else:
        index += flip
        if index < 0:
            index += 2
        elif index >= len(keys[part]):
            index -= 2
        c = keys[part][index]
        
    return c
    
def run(args):
    if type(args) is not list or len(args) < 2:
        print("usage: {} <percent> <args...>".format(__file__))
        exit(1337)
        
    percent = int(args[0]) % 100
    for cmd in args[1:]:
        cmd = list(cmd)
        for i in range(len(cmd)):
            if randint(1, 100) <= percent:
                cmd[i] = randChar(cmd[i])
        print("".join(cmd))
    
if __name__ == "__main__":
    import sys
    run(sys.argv[1:])