def name_value(my_list):
    lst = []

    for word in my_list:
        word = word.replace(" ", "")
        count = 0

        for char in word:
            count += ord(char.lower()) - 96

        lst.append(count)

    return lst
                
print(name_value(["abc","abc" "abc"]))