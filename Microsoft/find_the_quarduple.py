
# arr[] : int input array of integers
# k : the quadruple sum required

from collections import defaultdict


class Solution:
    def fourSum(self, nums, target):
        ans = []
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n-3:
            j = i+1
            while j < n-2:

                want = target-(nums[i]+nums[j])

                left = j+1
                right = n-1

                while left < right:

                    summ = nums[left]+nums[right]

                    if summ == want:
                        res = [nums[i], nums[j], nums[left], nums[right]]
                        # res.sort()
                        ans.append(res)

                        while left < right and nums[left] == res[2]:
                            left += 1

                        while left < right and nums[right] == res[3]:
                            right -= 1

                    elif summ < want:
                        left += 1
                    else:
                        right -= 1

                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            i += 1

        return ans


#{
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        n, k = map(int, input().split())
        # print(n, k)
        a = list(map(int, input().strip().split()))[:n]
        # print(a)
        ob = Solution()
        ans = ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans) == 0):
            print(-1, end="")
        print()


# } Driver Code Ends
