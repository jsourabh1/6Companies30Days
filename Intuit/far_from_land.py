class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        #         if grid.count(1)==0 or grid.count(0):

        #             return -1

        land = []
        m = n = len(grid)

        for i in range(len(grid)):

            for j in range(len(grid)):

                if grid[i][j] == 1:
                    land.append([i, j])

        if len(land) == m*n or len(land) == 0:
            return -1

        count = 0

        while land:

            size = len(land)

            for _ in range(size):

                i, j = land.pop(0)

                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x+i, y+j

                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        land.append((xi, yj))
                        grid[xi][yj] = 1
            count += 1
        return count-1
