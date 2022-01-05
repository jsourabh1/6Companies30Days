from collections import defaultdict


class Solution:
    def canPair(self, arr, k):
        # Code here

        for i in range(len(arr)):

            arr[i] = arr[i] % k

        dict_1 = defaultdict(lambda: 0)
        # print(arr)

        for i in arr:

            if i == 0:
                if dict_1[i] > 0:
                    dict_1[i] -= 1

                else:
                    dict_1[i] += 1

            elif dict_1[k-i] > 0:
                dict_1[k-i] -= 1

            else:
                dict_1[i] += 1
            # print(dict_1)

        for i in dict_1.values():

            if i > 0:
                return False

        return True


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
# } Driver Code Ends
