import sys
import math
import string
from decimal import Decimal
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    m, s = (sys.stdin.readline().rstrip()).split(" ")
    stuff = {}
    for i in range(int(m)):
        mat, r = (sys.stdin.readline().rstrip()).split(" ")
        stuff[str(mat)] = float(r)
    for i in range(int(s)):
        a, b, c = (sys.stdin.readline().rstrip()).split(" ")
        b, c, = float(b), float(c)
        if b*stuff[a] >= c:
            print("Infinity")
        else:
            res = Decimal(50/(c - b*stuff[a]))
            print(round(res, 2))
