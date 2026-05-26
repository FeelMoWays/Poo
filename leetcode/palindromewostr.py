class Solution:
    def isPalindrome(self,x: int) -> bool:
            lst = []
            if x < 0:
                return False
            while x > 0:
                digit = x % 10
                lst.append(digit)
                x = x//10
            if lst == lst[::-1]:
                 return True
            return False
            
        

print(Solution.isPalindrome(Solution,121))