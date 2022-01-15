from collections import defaultdict


class Solution:
    def isPossible(self, num, prer):
        #code here
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
        # print(q)
        result = []

        while q:

            current = q.pop(0)
            count += 1
            result.append(current)

            for i in graph[current]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        if len(result) != num:
            return False
        else:
            return True


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N = int(input())
        P = int(input())

        prerequisites = []
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob = Solution()
        if(ob.isPossible(N, prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
