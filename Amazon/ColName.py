alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Solution:
    def colName(self, num):

        global alpha
        # your code here

        if num < 26:
            return alpha[num-1]
        else:
            q, r = num//26, num % 26
            if r == 0:
                if q == 1:
                    return alpha[r-1]
                else:
                    return self.colName(q-1) + alpha[r-1]
            else:
                return self.colName(q) + alpha[r-1]


#{
#  Driver Code Starts
#Initial Template for Python 3

t = int(input())
for tc in range(t):
    n = int(input())
    ob = Solution()
    print(ob.colName(n))


# } Driver Code Ends
