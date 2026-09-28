class Solution:
    def countDigits(self, n):
        if n//10 == 0:
            return 1
        return 1 + self.countDigits(n//10)
m = Solution().countDigits(12312321)
print(m)