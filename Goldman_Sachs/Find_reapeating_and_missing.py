
class Solution:
    def findTwoElement(self, arr, n):
        ans = [False]*(n+1)
        first = 0
        for i in arr:
            if ans[i] == True:
                first = i
                5
            ans[i] = True
        second = 0

        for i in range(1, n+1):

            if ans[i] == False:
                second = i
                break
        return [first, second]

#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc = tc-1
# } Driver Code Ends
