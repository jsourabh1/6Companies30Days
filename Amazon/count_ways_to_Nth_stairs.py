
import sys
import io
import atexit


class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.

    # Returns no. of ways to
    # reach sth stair

    def countWays(self, s):

        mod = 1000000007
        # code here
        return (s//2)+1


#{
#  Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

# } Driver Code Ends
