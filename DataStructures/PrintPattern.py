class Solution:
    def pattern(self, n):
        if n < 0:
            return n
        if n == n:
            return n 
        ls = []
        if n > 0:
            ls.append(self.pattern(n-5))
        elif n == 0:
            ls.append(self.pattern(n+5))
        return ls
m = Solution().pattern(10)
print(m)