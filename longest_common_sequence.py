class Solution:
    def longestConsecutive(self,nums): 
        
        
        longest_length=0
        set_nums=set(nums)
        
        if len(nums)==0:
            return 0
        
        for num in nums:
            length=1
            if num-1 not in set_nums:  ##start element
                while num+1 in set_nums:  ##checking right neighbours
                    length+=1
                    num=num+1
            longest_length=length if length>longest_length else longest_length

        return longest_length

s=Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))