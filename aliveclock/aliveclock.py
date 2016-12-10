#!/usr/bin/env python3
import time
from random import randint
from datetime import datetime

def calcTime():
    count = 0
    goal = randint(30, 120)
    lastTick = int(time.time())
    while count < goal:
        now = int(time.time())
        if now > lastTick:
            count += 1
            lastTick = now
            yield "{}/{}".format(count, goal)
            
def run(args):
    if args is None:
        print("usage: {} <YYMMDD>".format(__file__))
        exit(1337)
    if type(args) is not list:
        args = [args]
        
    try:
        birthday = datetime.strptime(args[0], '%y%m%d').strftime('%Y-%m-%d')
    except ValueError as ve:
        print("Required date format: YYMMDD")
        exit(1337)
    except Exception as e:
        print("Exception: {}".format(e))
        exit(1337)

    print("Since your birthday is {} we need some time to calculate your alive clock...".format(birthday))
    for res in calcTime():
        print(res)
    print("According to our estimations you're actually alive now")

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])