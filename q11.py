import sys
import math
import string
from itertools import permutations
from decimal import Decimal
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    mm = (sys.stdin.readline().rstrip()).split(" ")
    #mm.sort(reverse=True)
    perm = permutations(mm)
    maxm = -1
    
    for i in list(perm):
        ans = ""
        for x in i:
            ans += x
        maxm = max(maxm, int(ans))

    print(maxm)
