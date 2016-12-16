#! /usr/bin/python2.7
import sys
if len(sys.argv) == 3:
    a = float(sys.argv[1]) + float(sys.argv[2])
    print(a)
else:
    print("usage: python3 solution.py OP1 OP2")
