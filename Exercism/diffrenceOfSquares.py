def square_of_sum(number):
    count = 0
    for i in range(number+1):
        count += i
    count = count ** 2
    return count


def sum_of_squares(number):
    count = 0
    for i in range(number+1):
        count += i**2
    return count

def difference_of_squares(number):
    return abs(sum_of_squares(number) - square_of_sum(number))
