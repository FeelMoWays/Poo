def find_it(seq):
    num_dict = {}
    for i in seq:
        num_count = seq.count(i)
        if i not in num_dict.keys():
            num_dict[i] = num_count
    for key , value in num_dict.items():
        if value % 2 != 0:
            return key
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))