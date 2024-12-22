import sys
import math
import string
from decimal import Decimal
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    w, it = sys.stdin.readline().rstrip().split(" ")
    w, it = int(w), int(it)
    area = (((3)**0.5)/4) * (w**2)
    for i in range(it):
        area = area*0.75
    print(f"{3**it} {round(Decimal(area), 2)}")
