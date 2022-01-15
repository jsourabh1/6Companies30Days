
import sys
from collections import OrderedDict


class Solution:

    #Function to find if the given edge is a bridge in graph.

    def bfs(self, vertex, adj, node):

        # ans.append(node)
        for i in adj[node]:

            if i not in vertex:

                vertex.add(i)
                self.bfs(vertex, adj, i)

    def isBridge(self, V, adj, c, d):
        # code here
        vertex1 = set()
        vertex1.add(c)
        self.bfs(vertex1, adj, c)
        adj[c].remove(d)
        if c in adj[d]:
            adj[d].remove(c)
        vertex = set()
        vertex.add(c)
        self.bfs(vertex, adj, c)
        # print(arr,arr1)
        if vertex == vertex1:
            return 0
        return 1


#{
#  Driver Code Starts
#Initial Template for Python 3

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
            adj[b].append(a)

        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i]))

        c, d = map(int, input().split())
        ob = Solution()

        print(ob.isBridge(V, adj, c, d))
# } Driver Code Ends
