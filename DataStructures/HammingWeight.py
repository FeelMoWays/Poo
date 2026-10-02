class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
m = Solution().hammingWeight(10011)
print(m)
