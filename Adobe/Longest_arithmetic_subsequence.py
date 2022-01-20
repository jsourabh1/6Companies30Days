
class Solution:
    def lengthOfLongestAP(self, nums, n):
        # code here

        if len(nums) <= 2:
            return len(nums)
        n = len(nums)
        dp = [{} for i in range(n)]
        results = 0

        for i in range(1, n):

            for j in range(i):

                diff = nums[i]-nums[j]

                if diff in dp[j]:

                    dp[i][diff] = dp[j][diff]+1

                else:
                    dp[i][diff] = 2

                results = max(results, dp[i][diff])

        return results


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(A, n)
        print(ans)
        tc -= 1

# } Driver Code Ends

