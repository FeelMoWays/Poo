for i in range (2,50):
    for n in range(2,i):
        if i % n == 0:
            print(f"{i} is not prime")
            break
    else:
        print("The Number is prime")
        

