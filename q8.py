import sys
import math
import string
from decimal import Decimal
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    v1, m1, v2, m2 = (sys.stdin.readline().rstrip()).split(",")
    v1, m1, v2, m2 = float(v1), float(m1), float(v2), float(m2)
    res = m1*v1 + m2*v2
    res = res/(m1+m2)
    print(round(Decimal(res), 2))
