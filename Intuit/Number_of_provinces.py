from collections import defaultdict


class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:

        graph = defaultdict(list)
        for i in range(len(grid)):

            for j in range(len(grid)):

                if grid[i][j] == 1:
                    graph[i].append(j)
        # print(graph)

        def helper(node, visited, graph):

            visited.add(node)

            for i in graph[node]:

                if i not in visited:
                    helper(i, visited, graph)

        visited = set()

        count = 0
        for i in range(len(grid)):

            if i not in visited:
                # print(visited)
                helper(i, visited, graph)

                count += 1

        return count
