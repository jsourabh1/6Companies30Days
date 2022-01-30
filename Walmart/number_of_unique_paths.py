
from ensurepip import version


# Memozation version

class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self, m, n):
        #code here
        if m == 1 and n == 1:
            return 1

        dp = [[-1]*(n+1) for i in range(m+1)]

        def helper(first, second):
            nonlocal m, n, dp

            if first == m and second == n:
                return 1
            if first > m or second > n:
                return 0
            if dp[first][second] != -1:
                return dp[first][second]

            dp[first][second] = helper(first+1, second)+helper(first, second+1)
            return dp[first][second]

        helper(1, 1)
        # print(dp)
        return dp[1][1]

#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends


# With top down approach


class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self, m, n):
        #code here
        if m == 1 and n == 1:
            return 1

        dp = [[-1]*(n+1) for i in range(m+1)]
        

        for i in range(1, m+1):

            for j in range(1, n+1):

                if i == j == 1:
                    dp[i][j] = 1

                elif j == 1:
                    dp[i][j] = 1

                elif i == 1:
                    dp[i][j] = 1

                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        # print(dp)
        return dp[-1][-1]

       
#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends
