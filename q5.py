import math

def nround(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

n = int(input())
for i in range(n):
    
    e = int(input())
    cmodel, csize, cweight, cpower, ccost = input().split(" ")
    csize, cweight, cpower, ccost = int(csize), int(cweight), int(cpower), int(ccost)
    ctotal = csize + cweight + cpower + ccost
    for i in range(e):
        model, size, weight, power, cost = input().split(" ")
        size, weight, power, cost = int(size), int(weight), int(power), int(cost)
        total = size + weight + power + cost
        if total <= nround(ctotal*0.8):
            cmodel, ctotal = model, total
    print(f"{cmodel} {ctotal}")
            
