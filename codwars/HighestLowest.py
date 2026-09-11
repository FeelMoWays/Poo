def high_and_low(numbers):
    numbers_strip = numbers.strip().split()

    highest = int(numbers_strip[0])
    lowest = int(numbers_strip[0])

    for i in numbers_strip:
        if int(i) > highest:
            highest = int(i)

        if int(i) < lowest:
            lowest = int(i)

    return str(highest), str(lowest)
#ChatGPT Answer