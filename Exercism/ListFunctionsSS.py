from functools import reduce
def append(list1, list2):
    list1.extend(list2)
    return list1

def concat(lists):
    list1 = []
    for i in lists:
        list1.extend(i)
    return list1


def filter(function, list):
    res = filter(function,list)
    return list(res)


def length(list):
    return len(list)


def map(function, list):
    res = map(function,list)
    return res


def foldl(function, list, initial):
    r = reduce(function,list,initial)
    return r


def foldr(function, list, initial):
    r  = reduce(function,reverse(list),initial)
    return r

def reverse(list):
    list.reverse()
    return list
