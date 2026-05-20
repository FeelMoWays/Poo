def isPalindrome(x: int) -> bool:
    u = str(x)
    if u[-1:] == u:
        return True
    else:
        return False
print(isPalindrome(121))