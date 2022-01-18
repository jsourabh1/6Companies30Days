from heapq import *
class Solution:
    def smallestRange(self, arr, n, k):
        # code here
        # print the smallest range in a new line
        maxx=-float("inf")

        minn=float("inf")
        
        min_range=[float("inf"),0,0]
        
        heap=[]
        heapify(heap)
        for i in range(k):
            
            heappush(heap,[arr[i][0],0,i])
            maxx=max(maxx,arr[i][0])
            
            
        while True:
            
            
            minn,index,listt=heappop(heap)
            
            if min_range[0]>maxx-minn+1:
                min_range[0]=maxx-minn+1
                min_range[1],min_range[2]=maxx,minn
                
                
            if index+1<n:
                
                heappush(heap,[arr[listt][index+1],index+1,listt])
                
                maxx=max(maxx,arr[listt][index+1])
            else:
                break
            
        return [min_range[2],min_range[1]]
                
                
                
                
            
            
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = Solution().smallestRange(numbers, n, k)
    print(r[0],r[1])
# } Driver Code Ends