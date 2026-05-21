def square_digits(num):
    count  = ""
    num = str(num)
    for i in num:
        i = int(i)
        u = i*i
        count += str(u)
    count = int(count)
    return count
print(square_digits(9919191))