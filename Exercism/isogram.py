def is_isogram(string):
    if string == "":
        return True
    string = string.lower()
    return len(set(string)) == len(string)
print(is_isogram('ltydteurocepiroycdvipuvl'))