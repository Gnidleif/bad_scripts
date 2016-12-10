#!/usr/bin/env python3
import sys
from random import randint

dick = {
    "balls": '8',
    "shaft": '=',
    "hand": 'm',
    "head": 'D',
    "cum": '~'
}

def pwdGen(low, high):
    final = randint(low, high)
    cum_len = randint(0, int(low/2))
    pen_len = (final - cum_len)
    
    penis = [dick['balls'], dick['head']]
    while len(penis) < pen_len:
        penis.append(dick['shaft'])
    penis[1], penis[-1] = penis[-1], penis[1]
    
    gripIndex = randint(1, pen_len - 2)
    penis[gripIndex] = dick['hand']
    
    if cum_len > 0:
        penis.append(''.join([dick['cum'] for x in range(cum_len)]))
        
    return ''.join(penis)
    
def run(args):
    if type(args) is not list or len(args) < 2:
        print("usage: {} <min-len> <max-len>".format(__file__))
        exit(1337)
        
    (low, high) = [int(x) for x in args[0:2]]
    if low < 5:
        low = 5
    if high < low:
        low, high = high, low
    
    pwd = pwdGen(low, high)
    print("Generated password: {}".format(pwd))

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
