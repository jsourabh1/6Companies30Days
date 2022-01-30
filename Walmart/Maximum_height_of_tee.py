
class Solution:
    def height(self, N):
        # code here

        # Sum of dots for height H <= N
        # H*(H + 1)/2 <= N
        # H*H + H – 2*N <= 0


        # Now by Quadratic formula
        # (ignoring negative root)

        # Maximum H can be(-1 + √(1 + 8N)) / 2

        ans = (-1+int((1+8*N)**0.5))//2
        return ans

#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.height(N))
# } Driver Code Ends
