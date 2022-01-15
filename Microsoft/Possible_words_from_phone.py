

import math


class Solution:

    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self, a, N):
        #Your code here
        dict_1 = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
                  6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        ans = []

        def helper(arr, string, index):

            nonlocal N, ans

            if index == N:
                ans.append(string)
                return

            for i in arr[index]:

                helper(arr, string+i, index+1)

        arr = []

        for i in a:
            arr.append(dict_1[i])

        helper(arr, "", 0)
        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):

        N = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a, N)
        for i in range(len(res)):
            print(res[i], end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
