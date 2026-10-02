import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        value = int(math.log2(n))
        return pow(2,value) == n
m = Solution().isPowerOfTwo(16)
print(m)

#Using Recursion 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base cases
        if n == 1:
            return True

        if n <= 0 or n % 2 != 0:
            return False

        # Recursive case
        return self.isPowerOfTwo(n // 2)