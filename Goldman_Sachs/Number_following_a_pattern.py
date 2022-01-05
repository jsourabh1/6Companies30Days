class Solution:
    def printMinNumberForPattern(ob, S):
        # code here

        count = 1

        stack = []

        ans = ""

        for i in S:

            if i == "D":
                stack.append(count)
                count += 1

            else:

                stack.append(count)
                count += 1

                while stack:
                    ans += str(stack.pop())
        stack.append(count)

        while stack:
            ans += str(stack.pop())

        # print(ans)
        return int(ans)


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
