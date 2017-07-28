#!/usr/bin/env python3
# Creds till @skilleras som jag snodde konceptet av
import re

def run(args):
    words = ' '.join(args)
    rgx = re.compile(r'\w')
    i = 0
    res = ''

    for c in words:
        m = re.match(rgx, c)
        if m is not None:
            i += 1
            c = c.upper() if i % 2 == 0 else c.lower()

        res += str(c)

    print(res)

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])
