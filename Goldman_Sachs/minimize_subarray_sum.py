class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ans=float("inf")
        sum=0
        i=j=0
        
        while i<len(nums):
            
            sum+=nums[i]
            
            while j<i and (sum-nums[j])>=target:
                sum-=nums[j]
                j+=1
                
            if sum>=target:
                ans=min(ans,i-j+1)
                
            # print(sum,i,j)
                
            i+=1
        # print(ans) 
        return ans if ans!=float(inf) else 0
                
            
        