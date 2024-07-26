'''


https://www.youtube.com/watch?v=xQ3vjWwFRuI&t=1587s
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
'''
import heapq
from collections import defaultdict
class Solution:
    def dijkstra(self,source,v,adj):
        result=[float('inf')]*v
        result[source]=0
        heap = []
        heapq.heappush(heap,(0,source))
        while heap:
            temp = heapq.heappop(heap)
            dist = temp[0]
            node = temp[1]
            for each in adj[node]:
                nei = each[0]
                weight = each[1]
                if weight+dist<result[nei]:
                    result[nei]=weight+dist
                    heapq.heappush(heap,(result[nei],nei))
        return result
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            adj[u].append((v,w))
            adj[v].append((u,w))
        length = len(adj)
        result=[]
        for i in range(n):
            result.append(self.dijkstra(i,n,adj))
        maxResult = -1
        maxCount  =n+1
        for i in range(n):
            count = 0
            for j in range(n):
                if result[i][j]<=distanceThreshold:
                    count +=1
            if maxCount>=count and maxResult<i:
                maxCount = count
                maxResult = i
        return maxResult

        
