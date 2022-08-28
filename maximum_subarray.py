

nums=[-2,-1 ,0]


class Solution:
   def maxSubArray(self, nums):
        
        max_sum=nums[0]
        sums=0
        
        for i in range(len(nums)):
            sums+=nums[i]
            sums=0 if sums<0 else sums
            if sums>0:
                max_sum=sums if sums>max_sum else max_sum

        if max_sum< max(nums):  ## for all negative numbers
            max_sum=max(nums)

       
        
        return max_sum
 
s=Solution()
print(s.maxSubArray( nums))
