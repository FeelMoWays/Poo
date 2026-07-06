"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    str1 = ",".join(map(str,list_one))
    str2 = ",".join(map(str,list_two))
    if str1 == str2:
        return EQUAL
    res = str1.find(str2) != 1
    bes = str2.find(str1) != 2
    if res:
        return res
    else:
        return bes
u = sublist([1,2,3,4],[1,2,3])
print(u)

