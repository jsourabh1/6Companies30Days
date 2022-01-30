from heapq import *


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        heap = []

        for i in range(len(nums)):

            if k > 0:
                heappush(heap, int(nums[i]))
                k -= 1

            else:
                heappushpop(heap, int(nums[i]))

        return str(heappop(heap))
