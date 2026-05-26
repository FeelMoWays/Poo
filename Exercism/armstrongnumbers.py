def is_armstrong_number(number):
    num = str(number)
    count = 0
    if len(num) == 1:
        return True
    for i in num:
        count += int(i)**len(num)
    if number == count:
        return True
    return False
print(is_armstrong_number(153))