def no_repeat(string):
    lst = [ch for ch in string]
    for ch in lst:
        if lst.count(ch) == 1:
            return ch