def pair(arr):
    count = 0
    for i in range(1,len(arr),2):
        if abs(arr[i]-arr[i+1]) == 1:
            count += 1
    return count