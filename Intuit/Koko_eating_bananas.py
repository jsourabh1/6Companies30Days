import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles)>=h:
            return max(piles)
        
        else:
            
            low=1
            high=max(piles)
            
            ans=float("inf")
            
            while low<=high:
                
                mid=(low+high)//2
                
                time=0
                
                for i in piles:
                    # print(math.ceil(i/mid))
                    time+=math.ceil(i/mid)
                    
                # print(time)
                    
                if time<=h:
                    
                    ans=min(ans,mid)
                    high=mid-1
                    
                else:
                    low=mid+1
                    
                # print(mid,low,high)
                # break
            return ans
                    
                    
                    
                    
            
            
            
        
        