import math
def moser():
    n = int(input("Enter how far"))
    i = 1
    lst = []
    while i != n:
        lst.append((math.comb(i,4) + math.comb(i,2) + 1))
        i += 1
    return lst
u = moser()
print(u)