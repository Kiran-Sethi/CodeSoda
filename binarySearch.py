def search(nums, target) :
          l, r=0,len(nums)-1
          
        
          while r>=l:
            mid=int((l+r)/2)
            print(nums[mid])
   
            if target==nums[mid]:
                print(nums[mid])
                return mid
            
            elif target<nums[mid]:
                r=mid-1
                
            elif target>nums[mid]:
                l=mid+1
                
        
          return -1
            
 
nums = [-1,0,3,5,9,12]
target =-17
print(search( nums, target) )

