def josephus(items, k):
    result = []
    pointer = 0

    while items:
        pointer = (pointer + k - 1) % len(items)
        result.append(items.pop(pointer))

    return result

