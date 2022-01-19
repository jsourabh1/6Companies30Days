
# first approach 
class Solution:
    def generateParenthesis(self, n: int):
        def generate(arr):
            nonlocal ans, n
            if len(arr) == 2*n:

                if valid(arr):
                    ans.append("".join(arr))

                return

            else:

                arr.append("(")
                generate(arr)
                arr.pop()

                arr.append(")")
                generate(arr)
                arr.pop()

        def valid(arr):

            count = 0

            for i in arr:

                if i == "(":
                    count += 1

                else:
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        ans = []
        generate([])
        return ans


# 2nd approach 







class Solution:
    def AllParenthesis(self, n):
        #code here

        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack([], 0, 0)
        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        n = int(input())
        ob = Solution()
        result = ob.AllParenthesis(n)
        result.sort()
        for i in range(0, len(result)):
            print(result[i])


# } Driver Code Ends
