from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for a, b in points:

            counter = {}

            for i, j in points:

                key = (a-i)**2+(j-b)**2

                if key in counter:

                    ans += 2*counter[key]

                    counter[key] += 1

                else:
                    counter[key] = 1

        return ans
