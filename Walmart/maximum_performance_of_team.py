from heapq import *


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        heap = []

        res = summ = 0

        for e, s in sorted(zip(efficiency, speed), reverse=True):

            heappush(heap, s)

            summ += s

            if len(heap) > k:
                summ -= heappop(heap)

            res = max(res, summ*e)

        return res % ((10**9)+7)
