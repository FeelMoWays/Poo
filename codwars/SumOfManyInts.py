def f(n: int, m: int) -> int:
    q , r = divmod(n,m)
    return q *m * (m-1)//2 + r * (r + 1) // 2
#The remainder pattern repeats every m numbers, so calculate the sum of each complete cycle using the arithmetic-series formula, then add the sum of the leftover remainders. 