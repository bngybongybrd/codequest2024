n = int(input())
for i in range(n):
    cords = int(input())
    x2, y2, d = input().split(" ")
    x2, y2, d = int(x2), int(y2), int(d)
    for i in range(cords):
        x, y = input().split(" ")
        x, y = int(x), int(y)
        dist = ((x2-x)**2 + (y2-y)**2)**0.5
        if dist >= d:
            print(f"({x},{y}) SAFE")
        else:
            print(f"({x},{y}) DANGER")
