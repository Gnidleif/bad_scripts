#!/usr/local/bin/python3.5
import sys
from random import randint

def scramble(cmd):
    calc = eval(cmd)
    if not isinstance(calc, int) and not isinstance(calc, float):
        raise TypeError("Incorrect type: {} - {}".format(calc, type(calc)))
        return
    
    isFloat = True if isinstance(calc, float) else False
    if isFloat:
        calc = int(str(calc).split('.')[1])
    
    calc = [b for b in bin(calc).split("0b")[1]]
    if len(calc) > 2:
        i = randint(0, len(calc) - 1)
        if calc[0] != calc[i]:
            calc[0], calc[i] = calc[i], calc[0]
        else:
            calc[i] = '1' if calc[0] == '0' else '0'
    else:
        calc[0] = '1' if calc[0] == '0' else '0'
    calc = int("0b{}".format("".join(calc)), 2)
    
    if isFloat:
        calc = float("0.{}".format(calc))
        
    return calc

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} <args..>".format(sys.argv[0]))
        
    for cmd in sys.argv[1:]:
        try:
            res = scramble(cmd)
        except Exception as e:
            print("Exception: {}\n".format(e))
            continue
        print("{} = {}".format(cmd, res))