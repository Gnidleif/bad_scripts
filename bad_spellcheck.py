#!/usr/local/bin/python3.5
import sys
from random import randint

def randChar(c):
    omit = " ,./?!'\""
    if c in omit:
        return c
        
    keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]
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
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: {} <percent> <args..>".format(sys.argv[0]))
        
    try:
        percent = int(sys.argv[1]) % 100
    except Exception as e:
        print("Exception: {}".format(e))
        sys.exit(1)
    
    for cmd in sys.argv[2:]:
        arr = [c for c in cmd]
        for i in range(len(arr)):
            if randint(1, 100) <= percent:
                arr[i] = randChar(arr[i])
        print("".join(arr))