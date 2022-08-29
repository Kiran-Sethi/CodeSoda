
class Solution:
  
    def twoSum(self, nums, target) :
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:  ##pair already seen
                return [i,dict[nums[i]]]

            else: ## pair has not occurred yet, append pair value:index of current
                 dict[target-nums[i]]=i

s=Solution()
print(s.twoSum([2,7,11,15],9) )               
