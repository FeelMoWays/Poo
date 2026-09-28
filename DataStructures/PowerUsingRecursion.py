class Solution:
    def recursivePower(self, n, p):
        if p == 0:
            return 1
        return n * self.recursivePower(n,p-1)
        
m = Solution().recursivePower(3,10)
print(m)