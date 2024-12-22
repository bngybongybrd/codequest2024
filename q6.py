import math

def nround(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

n = int(input())
for i in range(n):
    ip = input().split(".")
    for i in range(len(ip)):
        ip[i] = int(ip[i])
    flag = True
    if len(ip) != 4:
        flag = False
    for num in ip:
        if not (0 <= num <= 255):
            flag = False
    if flag:
        print("VALID")
    else:
        print("INVALID")
