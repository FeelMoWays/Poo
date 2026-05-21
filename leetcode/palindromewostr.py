
def isPalindrome( x: int) -> bool:
        lst = []
        while x > 0:
            digit = x % 10
            lst.append(digit)
            x = x//10
        lst.reverse()
       
        return lst
print(isPalindrome(3121))