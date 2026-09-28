class Solution:
    def isPalindrome(self,x: int) -> bool:
        if x < 0:
            return False
        u = str(x)
        o = int((u[::-1]))
        if o == x:
            return True
        return False
print(Solution.isPalindrome(Solution,121))