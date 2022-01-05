class Solution:
    def getNthUglyNo(self,n):
        # code here
        
        dp=[1]*n
        i2=i3=i5=0        
        for i in range(1,n):
            
            multiple_2=dp[i2]*2
            multiple_3=dp[i3]*3
            multiple_5=dp[i5]*5
            
            final=min(multiple_2,multiple_3,multiple_5)
            dp[i]=final
            if final==multiple_2:
                i2+=1
                
            if final==multiple_3:
                i3+=1
                
            if final==multiple_5:
                i5+=1
                
        return dp[-1]
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends