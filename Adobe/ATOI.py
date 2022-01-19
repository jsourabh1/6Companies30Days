class Solution:
    def atoi(self, string):

        ans = 0
        first = 1
        for i in string[::-1]:

            if i == "-":
                ans = ans-2*ans
            elif not i.isnumeric():
                return -1
            else:
                ans += int(i)*first
                first *= 10
        return ans

#{
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        ob = Solution()
        print(ob.atoi(string))
# } Driver Code Ends
