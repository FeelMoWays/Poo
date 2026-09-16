import math
def surjections(n: int, k: int) -> int:
    if n < k :
        return 0
    total = 0
    for i in range(k + 1):
        total += (-1) ** i * math.comb(k, i) * (k - i) ** n
    return total
print(surjections(3,2)) 
#Done by the principle of exclusion-inclusion