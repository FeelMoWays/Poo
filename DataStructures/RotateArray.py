def rotate_array(array,k):
    n = len(array)
    if array == []:
        return array
    else:
        for _ in range(k):
            last = array[n-1]
            for i in range(n-1,0,-1):
                array[i] = array[i-1]
            array[0] = last
        return array