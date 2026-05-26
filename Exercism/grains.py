def square(number):
    if number > 64 or number <= 0:
        raise ValueError("Square must be between 1 and 64")
    return 2**(number - 1)


def total():
    count = 0
    for i  in range(1,65):
        count += square(i)
    return count