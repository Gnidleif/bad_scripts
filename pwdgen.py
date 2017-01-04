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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: {} <min-len> <max-len>".format(sys.argv[0]))
        exit(1337)
    
    (low, high) = [int(x) for x in sys.argv[1:3]]
    if low < 5:
        low = 5
    if high < low:
        low, high = high, low
    
    pwd = pwdGen(low, high)
    print("Generated password: {}".format(pwd))
