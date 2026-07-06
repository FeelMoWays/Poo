def is_isogram(string):
    string = string.lower()
    string= string.replace(" ","")
    string = string.replace("-","")
    sets = set(string)
    return len(sets) == len(string)