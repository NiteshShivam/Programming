'''
https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1

'''
from collections import defaultdict,deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj = defaultdict(list)
        for each in edges:
            adj[each[0]].append(each[1])
            adj[each[1]].append(each[0])
        result = [float('inf')]*n
        result[src]=0
        q = deque()
        q.append(src)
        while q:
            length = len(q)
            while length:
                vertex = q.popleft()
                for each in adj[vertex]:
                    if result[vertex]+1<result[each]:
                        result[each]=1+result[vertex]
                        q.append(each)
                length-=1
        for i in range(n):
            if result[i]==float('inf'):
                result[i] =-1
        return result
                
