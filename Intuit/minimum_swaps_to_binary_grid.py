class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        swaps = 0
        zeroesNeeded = len(grid)-1
        start = 1

        for i in range(len(grid)):
            temp = i
            while temp < len(grid) and grid[temp][start:] != [0]*zeroesNeeded:
                temp += 1

            if temp >= len(grid):
                return -1

            start += 1
            zeroesNeeded -= 1

            while temp > i:
                grid[temp], grid[temp-1] = grid[temp-1], grid[temp]
                temp -= 1
                swaps += 1

        return swaps
