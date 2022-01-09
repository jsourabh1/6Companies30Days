# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:

#         queue = []

#         row = [-1, 0, 1, 0]
#         col = [0, -1, 0, 1]
#         count = 0
#         for i in range(len(grid)):

#             for j in range(len(grid[0])):

#                 if grid[i][j] == 2:
#                     queue.append([i, j])

#                 if grid[i][j] == 1:
#                     count += 1
#         time = 0
#         while queue:


#             changed = False

#             n = len(queue)

#             while n:

#                 first, second = queue.pop(0)

#                 for i in range(4):
#                     r = row[i] + first
#                     c = col[i] + second

#                     if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1:
#                         changed = True
#                         grid[r][c] = 2
#                         queue.append([r, c])
#                         count -= 1
#                 n -= 1

#             if not changed:
#                 break
#             time += 1

#         if count != 0:
#             return -1

#         return time

def check(S, W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]: return False
            while i2 < n and S[i2] == S[i]: i2 += 1
            while j2 < m and W[j2] == W[j]: j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False
            i, j = i2, j2
        return i == n and j == m



def expressive_cnt(S,inp):

    count=0

    for i in inp:

        if check(S,i):
            count+=1

    return count

print(expressive_cnt("wuuusssuup",['wusuuup',"wuusuup"]))