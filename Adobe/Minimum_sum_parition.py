   
class Solution: 
    def equalPartition(self, N, arr):
        # code here
        
        if sum(arr)%2!=0:
            return False
            
        want=sum(arr)//2
        
        dp=[[0]*(want+1) for i in range(N+1)]
        
        
        for i in range(N+1):
            
            for j in range(want+1):
                
                if i==0 and j==0:
                    dp[i][j]=True
                    
                elif i==0:
                    dp[i][j]=False
                elif j==0:
                    dp[i][j]=True
                    
                elif j>=arr[i-1]:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[-1][-1]

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends