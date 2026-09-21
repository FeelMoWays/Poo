def find_number(sums):
    ls = list(map(int,str(sums).strip()))
    sumss = []
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            sumss.append(ls[i] + ls[j])
    return sumss
print(find_number(3264128))