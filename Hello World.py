def comp(array1,array2):
    array1 = array1[-1:] + array1[:-1]
    for i in array1:
        for j in array2:
            if (i*i) != j:
                return False
            else:
                return True
u = comp([11,12,13,11],[121,121,144,169])
if u == True:
    print("good")
else:
    print("not")