from heapq import *
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        heap=[]
        
        for i in range(k):
            heappush(heap,(-arr[i],i))
        res=[]
        res.append(-heap[0][0])
        for i in range(k,len(arr)):
            heappush(heap,(-arr[i],i))
            res.append(self.get_max(heap,i-k+1))
            
        return res
        
        
    def get_max(self,heap,start):
        
        while True:
            val,index=heap[0]
            
            if index>=start:
                return  -val
            heappop(heap)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends