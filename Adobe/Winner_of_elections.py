from collections import defaultdict


class Solution:

    #Complete this function

    #Function to return the name of candidate that received maximum votes.
    def winner(self, arr, n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved

        dict_1 = defaultdict(lambda: 0)

        max = 0
        ans = []
        for i in arr:
            dict_1[i] += 1

            if dict_1[i] > max:
                max = dict_1[i]
                ans = []
                ans.append(i)
            elif dict_1[i] == max:
                ans.append(i)
            # print(ans)
        # print(dict_1,ans)
        ans.sort()
        # print(ans)
        return ans[0], dict_1[ans[0]]


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):

        n = int(input())
        arr = input().strip().split()

        result = Solution().winner(arr, n)
        print(result[0], result[1])
# } Driver Code Ends
