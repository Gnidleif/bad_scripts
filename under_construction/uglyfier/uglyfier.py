#!/usr/bin/env python3
import sys
import json
import re

def init(type):
    with open('lookup.json', 'r') as f:
        regexes = json.load(f)
        
    if type not in regexes.keys():
        print("Supported formats: {}".format([x for x in regexes.keys()]))
        return None
    
    regexes = regexes[type]
    for i in range(len(regexes)):
        try:
            regexes[i] = re.compile(regexes[i], flags=re.I)
        except TypeError as te:
            print("Arg: [{}] raised TypeError: {}".format(regexes[i], te))
            return None
    return regexes

def produce(data, regexes):
    switches = {}
    processed = data
    for r in regexes:
        for s in re.findall(r, data):
            switches[s] = ""
    
    return processed

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: {} <source> <destination>".format(sys.argv[0]))
        exit(1337)
    
    src, dst = sys.argv[1], sys.argv[2]
    type = src.split('.')[-1]
    regexes = init(type)
    if regexes is None:
        exit(1337)
        
    with open(src, 'r') as f:
        data = f.read()
    
    with open(dst, 'w') as f:
        f.write("{}\n".format(produce(data, regexes)))