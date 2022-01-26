class Solution:
    def shipWithinDays(self, arr: List[int], m: int) -> int:
        low = max(arr)
        high = sum(arr)
        ans = 0
        while low <= high:

            mid = (low + high) // 2

            count = 1
            summ = 0
            for i in arr:
                if (summ + i) > mid:
                    count += 1
                    summ = i
                else:
                    summ += i
            if count <= m:
                ans = mid
                high=mid-1
           
            else:
                low = mid + 1

        return ans
            