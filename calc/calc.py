#!/usr/bin/env python3

def scramble(cmd):
    calc = eval(cmd)
    if isinstance(calc, int):
        calc = handleInt(calc)
    elif isinstance(calc, float):
        calc = handleFloat(calc)
    else:
        raise TypeError("Incorrect type: {} - {}".format(calc, type(calc)))
    return calc

def handleFloat(num):
    (head, tail) = [str(handleInt(int(i))) for i in str(num).split('.')]
    return float("{}.{}".format(head, tail))

def handleInt(num):
    calc = [b for b in bin(num).split('0b')[1]]
    if len(calc) >= 2:
        index = int(len(calc) / 2)
        if calc[0] != calc[index]:
            calc[0], calc[index] = calc[index], calc[0]
        else:
            calc[index] = '1' if calc[index] == '0' else '0'
    else:
        calc[0] = '1' if calc[0] == '0' else '0'
    return int("0b{}".format(''.join(calc)), 2)

def run(args):
    if args is None:
        print("usage: {} <args..>".format(__file__))
        exit(1337)
    if type(args) is not list:
        args = [args]
        
    for cmd in args:
        try:
            res = scramble(cmd)
        except TypeError as te:
            print("TypeError: {}".format(te))
            continue
        except Exception as e:
            print("Exception: {}".format(e))
            continue
        print("{} = {}".format(cmd, res))
    

if __name__ == "__main__":
    import sys
    run(sys.argv[1:])