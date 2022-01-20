def power(x,y,p):
    res = 1
    x = x % p

    if (x == 0):
        return 0

    while (y > 0):
        if (y & 1):
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p

    return res


class Solution:
    def kvowelwords(self, N, K):
        # code here

        i, j = 0, 0
        MOD = 1000000007

        # Array dp to store number of ways
        dp = [[0 for i in range(K + 1)]
              for i in range(N + 1)]

        sum = 1
        for i in range(1, N + 1):

            #dp[i][0] = (dp[i-1][0]+dp[i-1][1]..dp[i-1][k])*21
            dp[i][0] = sum * 21
            dp[i][0] %= MOD

            # Now setting sum to be dp[i][0]
            sum = dp[i][0]

            for j in range(1, K + 1):

                # If j>i, no ways are possible to create
                # a string with length i and vowel j
                if (j > i):
                    dp[i][j] = 0
                elif (j == i):

                    # If j = i all the character should
                    # be vowel
                    dp[i][j] = power(5, i, MOD)
                else:

                    # dp[i][j] relation with dp[i-1][j-1]
                    dp[i][j] = dp[i - 1][j - 1] * 5

                dp[i][j] %= MOD

                # Adding dp[i][j] in the sum
                sum += dp[i][j]
                sum %= MOD

        return sum


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        ob = Solution()
        ans = ob.kvowelwords(N, K)
        print(ans)
# } Driver Code Ends
