
# Python 3
from bisect import bisect_left

# Function to find LIS in O(nlogn) time


def LongestIncreasingSubsequenceLength(nums):

    sub = []
    for x in nums:
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)
        else:
            # Find the index of the smallest number >= x
            idx = bisect_left(sub, x)
            sub[idx] = x  # Replace that number with x

    return len(sub)


class Solution:
    def minInsAndDel(self, arr, brr, N, M):
        # Find LCS using LIS
        vec = []
        s = set(brr)
        for i in arr:
            if i in s:
                vec.append(i)
        # print(vec)
        res = LongestIncreasingSubsequenceLength(vec)
        return abs(N - res) + abs(M - res)

#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        ob = Solution()
        print(ob.minInsAndDel(A, B, N, M))
# } Driver Code Ends
