import math 
"""
Input:  two non-negative integers a and b, satisfying a >= b.
Output: a tuple (x, y) satisfying gcd(a, b) = x*a + y*b.
"""
def gcd_coeff(a: int, b: int) -> tuple:
    d = math.gcd(a,b)
    