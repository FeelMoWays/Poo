def even_last(numbers):
    count = 0
    if numbers == []:
        return 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            count += numbers[i]
    count = count * numbers[-1]
    return count
print(even_last([2, 3, 4, 5]))

