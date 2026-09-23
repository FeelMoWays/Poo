#Worst Case
# def max_area(array):
#     n = len(array)
#     temp = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             area = min(array[i],array[j]) * (j-i)
#             temp = max(area,temp)
#     return temp

#Best Case
def max_area(array):
    n = len(array)
    temp = 0
    right = n-1
    left = 0
    while left < right:
        amount = min(array[left],array[right])* (right-left)
        temp = max(amount,temp)
        if array[left]>array[right]:
            right -= 1
        else:
            left += 1
    return temp    
