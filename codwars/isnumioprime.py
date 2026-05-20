def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True
u = is_prime(9)
if u:
    print("good")
else:
    print("not")