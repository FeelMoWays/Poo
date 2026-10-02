import math 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        value  = round(math.log(n,3))
        return pow(3,value) == n
m = Solution().isPowerOfThree(243)
print(m)
# Recursion
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n <=0 or n%3 != 0:
            return False
        return self.isPowerOfThree(n//3)

        