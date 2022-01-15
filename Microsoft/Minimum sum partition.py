class Solution:
    def minDifference(self, arr, n):

        ans = (1+sum(arr))//2

        dp = [[-1]*(ans+1) for i in range(n+1)]

        for i in range(n+1):

            for j in range(ans+1):

               if i == 0 and j == 0:
                   dp[i][j] = 1

               elif j == 0:
                   dp[i][j] = 1

               elif i == 0:

                   dp[i][j] = 0

               elif arr[i-1] <= j:

                   dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]

               else:
                   dp[i][j] = dp[i-1][j]

    #     print(dp)
        minn = float("inf")

        for i in range(ans+1):

            if dp[n][i]:

                minn = min(minn, abs(sum(arr)-2*i))

        return minn


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)

# } Driver Code Ends
