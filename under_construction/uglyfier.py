#!/usr/bin/env python3
import sys
import json
import re

def produce(data, regexes):
    to_switch = {}
    processed = data
    for r in regexes:
        for s in re.findall(r, data):
            to_switch[s] = ""
    
    return processed

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: {} <source> <destination>".format(sys.argv[0]))
        exit(1337)
    
    src, dest = sys.argv[1], sys.argv[2]
    type = src.split('.')[-1]
    with open('lookup.json', 'r') as f:
        regexes = json.load(f)
        
    if type not in regexes.keys():
        print("Supported formats: {}".format([x for x in regexes.keys()]))
        exit(1337)
    
    regexes = regexes[type]
    for i in range(len(regexes)):
        try:
            regexes[i] = re.compile(regexes[i], flags=re.I)
        except TypeError as te:
            print("Arg: [{}] raised TypeError: {}".format(regexes[i], te))
            exit(1337)
        
    with open(src, 'r') as f:
        data = f.read()
    
    result = produce(data, regexes)