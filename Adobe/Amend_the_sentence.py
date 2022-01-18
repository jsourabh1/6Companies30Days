
class Solution:

    def amendSentence(self, s):

        # code here

        ans = ""
        string = ""

        for i in range(len(s)):

            if 97 <= ord(s[i]) <= 122:
                string += s[i]
            else:
                if string:
                    ans += string
                    ans += " "

                string = ""
                string += s[i].lower()
        ans += string
        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.amendSentence(s))


# } Driver Code Ends
