def is_prime(num):
    '''To check the prime of a number'''
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
       
            
    return True