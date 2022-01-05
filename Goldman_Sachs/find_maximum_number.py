# We have given 10Million enteries and we have to find the 10 maximum number so we have different methods
# 1) First Method:- Sorting(O(nlogn))

def solve(arr):

    arr.sort(reverse=True)

    return arr[:10]


#2) Second Method :- using priority Queue (nlogK) where k=10 is the size of the queue
from heapq import *
def solve1(arr):
    heap=[]
    for i in range(10):
        heappush(heap,arr[i])

    for i in range(10, len(arr)):

        heappushpop(heap,arr[i])
    # print(heap)
    return heap


#Example 
solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 2, 2, 2, 2])

solve1([1,2,3,4,5,6,7,8,9,0,2,2,2,2,2])


