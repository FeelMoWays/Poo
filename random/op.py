
def twoSum(nums, target):
    sut = []
    i = 0
    while i < len(nums):
        j = 0

        while j < len(nums):
            if i != j and nums[i] + nums[j] == target:
                sut.append(i)
                sut.append(j)
                
            j += 1

        i += 1
        return sut
u = twoSum([10,12,13],25)
print(u)
