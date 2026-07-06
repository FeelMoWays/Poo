def swap(number):
    digits = list(str(number))
    maximum = "".join(sorted(digits, reverse=True))

    if digits[0] == "0":
        for i in range(1,len(digits)):
            if digits[i] != "0":
                digits[0], digits[i] = digits[i], digits[0]
                break
    minimum = "".join(sorted(digits))
    return int(maximum), int(minimum)
