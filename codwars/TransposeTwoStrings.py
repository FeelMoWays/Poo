def transpose_two_strings(arr):
    string1 = arr[0]
    string2 = arr[1]
    if len(string1) > len(string2):
        string2 += " " * (len(string1) - len(string2))
    elif len(string2) > len(string1):
        string1 += " " * (len(string2) - len(string1))
    transposed = []
    for i in range(len(string1)):
        transposed.append(string1[i] + " " + string2[i])
    return "\n".join(transposed)

#better method
from itertools import zip_longest

def transpose_two_strings(lst):
    return "\n".join(f"{a} {b}" for a, b in zip_longest(*lst, fillvalue=" "))