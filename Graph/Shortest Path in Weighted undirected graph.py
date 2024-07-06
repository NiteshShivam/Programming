#User function Template for python3
'''
You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights.
Find the shortest path between the vertex 1 and the vertex n,
if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. 
If no path exists,
then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Question
https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1
Solution:
https://www.youtube.com/watch?v=icVJUN45f1E
'''
from typing import List
import heapq
import sys
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        #adj = [[] for _ in range(n+1)] # this is also ok
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        pq = []
        result = [sys.maxsize]*(n+1)
        parent = [i for i in range(n+1)]
        S = 1
        result[S]=0
        parent[1]=1
        heapq.heappush(pq,(0,S))
        while pq:
            distance,source = heapq.heappop(pq)
            for each in adj[source]:
                adjNode = each[0]
                weight = each[1]
                if distance+weight<result[adjNode]:
                    parent[adjNode] = source
                    result[adjNode]=distance+weight
                    heapq.heappush(pq,(distance+weight,adjNode))
        if result[n]==sys.maxsize:
            return [-1]
        
        path = []
        node = n
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.append(result[n])
        
        # Return the path in the correct order
        return path[::-1]
   
