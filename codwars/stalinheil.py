def stalin_sort(arr):
    op =[]
    u = arr[0]
    op.append(u)
    for i in arr:
        for j in arr:
            if j >i:
                if i and j not in op:
                    op.append(j)
    return op
print(stalin_sort([3, 1, 4, 1, 5, 9, 2]))

    