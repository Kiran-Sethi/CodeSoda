

# nums=[0,1,0,2,1,0,1,3,2,1,2,1]
nums=[4,2,0,3,2,5]

def trap_rain_water(nums):
    start=0
    end=0
    i=0
    trapped=0
    temp_trapped=0
    while i<len(nums)-1:
        ###check increase increase to identify the start
        while (i<len(nums)-1) and (nums[i+1]>nums[i]):
                i+=1
                start=i
        if start==len(nums)-1:
                return trapped
        
        end=start 

        ### check decrease
        while  (i<len(nums)-1) and (nums[i+1]<=nums[i]):
                i+=1
                end=i
        
        if end==len(nums)-1: ##if this groove only decrease
          return trapped

        ## check now increase to find the end
        while (i<len(nums)-1) and (nums[i+1]>nums[i]):
            i+=1
            end=i
                 

        trapped+=(min(nums[start],nums[end])*(end-start-1)) - sum(nums[start+1:end])
        print(start,end,trapped)   
        start=end
        i=end


trap_rain_water(nums)





