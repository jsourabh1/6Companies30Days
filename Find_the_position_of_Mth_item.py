
class Solution:
    def findPosition(self, N, M, K):

        if N == 1:
            return N
        # code here
        temp = (M % N+K-1)

        return temp if temp <= N else temp % N

#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, K = map(int, input().split())

        ob = Solution()
        print(ob.findPosition(N, M, K))
# } Driver Code Ends
