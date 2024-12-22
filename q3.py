import math

n = int(input())

def nround(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

for i in range(n):
    income = int(input())
    if income <= 11000:
        print(nround(income*0.1))
    elif income <= 44725:
        print(nround(income*0.12))
    elif income <= 95375:
        print(nround(income*0.22))
    elif income <= 182100:
        print(nround(income*0.24))
    elif income <= 231250:
        print(nround(income*0.32))
    elif income <= 578125:
        print(nround(income*0.35))
    else:
        print(nround(income*0.37))
        
