def snail_length(x, y):
    if x == 0 and y == 0:
        return 0
    n = max(abs(x),abs(y))
    base = (((2*n)-1) ** 2) + 2
    if y == n:
        return base + (n-x)
    if x == -n:
        return base + 2*n+(n-y)
    if y == -n:
        return base + 4*n + (x+n)
    return base + 6*n + (y+n)