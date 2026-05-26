def has_subpattern(strng):
    n = len(strng)
    for k in range(1,n//2 + 1):
        if n % k == 0:
            s = strng[:k]
            if s * (n//k) == strng:
                return True
    return False
