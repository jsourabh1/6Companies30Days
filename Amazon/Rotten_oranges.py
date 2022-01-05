class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = []

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]
        count = 0
        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 2:
                    queue.append([i, j])

                if grid[i][j] == 1:
                    count += 1
        time = 0
        while queue:

            changed = False

            n = len(queue)

            while n:

                first, second = queue.pop(0)

                for i in range(4):
                    r = row[i] + first
                    c = col[i] + second

                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1:
                        changed = True
                        grid[r][c] = 2
                        queue.append([r, c])
                        count -= 1
                n -= 1

            if not changed:
                break
            time += 1

        if count != 0:
            return -1

        return time
