from collections import defaultdict


class Solution:
    def findOrder(self, num: int, prer: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0]*num

        for first, second in prer:

            graph[first].append(second)
            indegree[second] += 1

        # print(graph)

        q = []
        count = 0
        for i in range(num):
            if indegree[i] == 0:
                q.append(i)
        print(q)
        result = []

        while q:

            current = q.pop(0)
            count += 1
            result.append(current)

            for i in graph[current]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        if count != num:
            return []
        else:
            return result[::-1]
