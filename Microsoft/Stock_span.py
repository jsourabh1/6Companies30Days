

import sys
import io
import atexit


class Solution:

    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self, a, n):

        arr = []

        for i in a:
            arr.append([i, 1])
        stack = []
        ans = []
        for i, cost in arr:

            count = cost

            while stack and stack[-1][0] <= i:
                count += stack.pop()[1]

            ans.append(count)
            stack.append([i, count])

        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n)
        print(*ans)  # print space seperated elements of span array
# } Driver Code Ends
