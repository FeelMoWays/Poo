
def sum_factorial(lst):
    count = 0
    for i in lst:
        f = 1
        for j in range(1,i+1):
            f *= j
        count += f
    return count
print(sum_factorial([4,6]))