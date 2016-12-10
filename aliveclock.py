#!/usr/bin/env python3
import sys
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

if __name__ == "__main__":
        if len(sys.argv) < 2:
            print("usage: {} <YYMMDD>".format(sys.argv[0]))
            sys.exit(1337)

        try:
            birthday = datetime.strptime(sys.argv[1], '%y%m%d').strftime('%Y-%m-%d')
        except ValueError as ve:
            print("Required date format: YYMMDD")
            sys.exit(1337)
        except Exception as e:
            print("Exception: {}".format(e))
            sys.exit(1337)

        print("Since your birthday is {} we need some time to calculate your alive clock...".format(birthday))
        for res in calcTime():
            print(res)
        print("According to our estimations you're actually alive now")
