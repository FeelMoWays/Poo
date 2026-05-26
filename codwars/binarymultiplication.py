def bin_mul(a, b):
    m = max(a, b)
    n = min(a, b)

    lst = []

    while m > 0:
        if m % 2:
            lst.append(n)
        m //= 2
        n *= 2

    return sorted(lst, reverse=True)
print(bin_mul(1325,960))
