def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
print(flatten([1, [2, 6], [[[4]], 5]]))