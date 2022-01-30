

import sys


class Solution:
    def find3number(self, A, n):
        # code here

        n = len(arr)

# Index of maximum element from right side
        max = n-1

    # Index of minimum element from left side
        min = 0

        # Create an array that will store
        # index of a smaller element on left side.
        # If there is no smaller element on left side,
    # then smaller[i] will be -1.
        smaller = [0]*10000
        smaller[0] = -1
        for i in range(1, n):
            if (arr[i] <= arr[min]):
                min = i
                smaller[i] = -1
            else:
                smaller[i] = min

        # Create another array that will
        # store index of a greater element
        # on right side. If there is no greater
    # element on right side, then greater[i]
    # will be -1.
        greater = [0]*10000
        greater[n-1] = -1

        for i in range(n-2, -1, -1):
            if (arr[i] >= arr[max]):
                max = i
                greater[i] = -1

            else:
                greater[i] = max

        # Now find a number which has
        # both a greater number on right
    # side and smaller number on left side
        for i in range(0, n):
            if smaller[i] != -1 and greater[i] != -1:
                return [arr[smaller[i]], arr[i], arr[greater[i]]]

        # If we reach here, then there are no such 3 numbers

        return []

#{
#  Driver Code Starts
#Initial Template for Python 3


sys.setrecursionlimit(100000)


def isSubSeq(arr, lis, n, m):
    if m == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] == lis[m-1]:
        return isSubSeq(arr, lis, n-1, m-1)
    return isSubSeq(arr, lis, n-1, m)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = Solution().find3number(arr, n)
    # print(lis)
    # print(isSubSeq(arr, lis, n, len(lis)))
    if len(lis) != 0 and len(lis) != 3:
        print(-1)
        continue
    if len(lis) == 0:
        print(0)
    elif lis[0] < lis[1] and lis[1] < lis[2] and isSubSeq(arr, lis, n, len(lis)):
        print(1)
    else:
        print(-1)

# } Driver Code Ends
