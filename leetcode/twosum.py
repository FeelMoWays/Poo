class Solution:
    def twoSum(self,nums: List[int],target: int) -> List[int]:
        soul = []
        for i in range(len(nums)):
            x = nums[i]
            for j in range(i+1 , len(nums)):
                u = nums[j]
                if x + u == target:
                    if i not in soul:
                        soul.append(i)
                        
                    if j not in soul:
                        soul.append(j)
                        
        return soul
print(Solution.twoSum(Solution,[3,2,4],6))
       