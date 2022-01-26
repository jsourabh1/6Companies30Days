# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, obj: 'MountainArray') -> int:

        low = 0
        high = obj.length()-1

        peak = -1
        while low < high:

            mid = (low+high)//2

            if obj.get(mid) < obj.get(mid+1):
                low = peak = mid+1

            else:
                high = mid

        low = 0
        high = peak
        print(peak)

        while low <= high:

            mid = (low+high)//2
            # print(mid)

            if obj.get(mid) == target:
                return mid

            elif obj.get(mid) < target:
                low = mid+1
            else:
                high = mid-1

        low = peak+1
        high = obj.length()-1

        while low <= high:

            mid = (low+high)//2
            # print(mid)

            if obj.get(mid) == target:
                return mid

            elif obj.get(mid) > target:
                low = mid+1
            else:
                high = mid-1
        return -1
