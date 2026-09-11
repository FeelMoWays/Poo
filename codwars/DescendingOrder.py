def descending_order(num):
    str_num = str(num)
    ls = []
    for i in str_num:
        ls.append(int(i))
    ls.sort(reverse=True)
    res = list(map(str , ls))
    answer = ''.join(res)
    return int(answer)

#Easier Way
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))