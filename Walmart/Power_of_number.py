# import math
class Solution:
    #Complete this function
    def power(self,x,y):
        #Your code here
    
        if(y == 0): return 1
        temp = self.power(x, int(y / 2)) 
          
        if (y % 2 == 0):
            return (temp * temp)%((10**9)+7)
        else:
            if(y > 0): return (x * temp * temp)%((10**9)+7)
            else: return ((temp * temp) / x)%((10**9)+7)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends