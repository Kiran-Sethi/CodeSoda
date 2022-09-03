class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxm=0
        l=0
        r=len(height)-1
        while l!=r:
            area=(r-l)*min(height[r],height[l])
            maxm=area if area>maxm else maxm
            if height[r]>height[l]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            elif height[r]==height[l]:
                maxm_neighbour=max(height[l+1],height[r-1])
                if maxm_neighbour==height[l+1]:
                    l+=1
                else :
                    r-=1
        
        return maxm
 