class Solution:
    def maxCoins(self,arr, n):
        # Code here
        
        dp=[[0]*(n) for i in range(n)]
        
        for k in range(n):
            i=0
            j=k
            
            while i<n and j<n:
                # print(i,j)
                
                
                if i==j:
                    dp[i][j]=arr[i]
                    
                elif j-i==1:
                    dp[i][j]=max(arr[i],arr[j])
                else:
                    # print(i,j)
                    first=arr[i]+min(dp[i+2][j],dp[i+1][j-1])
                    second=arr[j]+min(dp[i+1][j-1],dp[i][j-2])
                    dp[i][j]=max(first,second)
                    
                i+=1
                j+=1
                
                    
        # print(dp)            
        return dp[0][-1]
            
        
 

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends

#             then take the max from the both ans
#                 take the worst(min) from both side 
#             i+2-----j  i+1---j-1     i+1-----j-1     i-----j-2
# oppo. select i+1   \     / select j select i \       /
#                     \   /                     \     /
# opponent turn    i+1-------j                 i-------j-1
# if we select the i   \                         / if we select the j
#                       \                       /
#             # i-----------------------------------j