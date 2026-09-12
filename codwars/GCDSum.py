def solve(s,g):
    if s % g != 0:
        return -1
    a = g
    b = s - a
    return a,b