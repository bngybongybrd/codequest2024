n = int(input())
for i in range(n):
    al = {}
    tc = input()
    for letter in tc:
        if letter == " ":
            continue
        if letter in al:
            al[letter] += 1
        else:
            al[letter] = 1
    maxm = -1
    for letter in al:
        if al[letter] > maxm:
            maxm = al[letter]
    print(maxm)
        
    
