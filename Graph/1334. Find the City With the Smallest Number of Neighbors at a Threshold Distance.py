'''


https://www.youtube.com/watch?v=xQ3vjWwFRuI&t=1587s

https://youtu.be/8YdqvOKViWA
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


====================================================================
import heapq
from collections import defaultdict
class Solution:
    def dijkstra(self,source,adj,result):
        for i in range(len(result)):
            result[i]=float('inf')
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
    def findResult(self,n,spm,distanceThreshold):
        maxResult = -1
        maxCount  =n+1
        for i in range(n):
            count = 0
            for j in range(n):
                if spm[i][j]<=distanceThreshold:
                    count +=1
            if maxCount>=count:
                maxCount = count
                maxResult = i
        return maxResult

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        spm = [[0]*n for i in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            adj[u].append((v,w))
            adj[v].append((u,w))
        length = len(adj)
        for i in range(n):
            self.dijkstra(i,adj,spm[i])
        #self.floyd_warshall(adj,spm)
        return self.findResult(n,spm,distanceThreshold)
        
        
        

=====================================================
import heapq
from collections import defaultdict
class Solution:
    def bellman(self,S,edges,distance):
        V = len(distance)
        distance[S]=0
        for i in range(V-1):
            for each in edges:
                u = each[0]
                v = each[1]
                w = each[2]
                if distance[u]!=self.biValue and distance[u]+w<distance[v]:
                    distance[v]=distance[u]+w
                # because it is bi-directional
                if distance[v]!=self.biValue and distance[v]+w<distance[u]:
                    distance[u] = distance[v]+w
        
    def findResult(self,n,spm,distanceThreshold):
        maxResult = -1
        maxCount  =n+1
        for i in range(n):
            count = 0
            for j in range(n):
                if spm[i][j]<=distanceThreshold:
                    count +=1
            if maxCount>=count:
                maxCount = count
                maxResult = i
        return maxResult

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        self.biValue = 10**9+7
        spm = [[self.biValue]*n for i in range(n)]
        for i in range(n):
            self.bellman(i,edges,spm[i])
        return self.findResult(n,spm,distanceThreshold)
        
        



=========================================================
from collections import defaultdict
class Solution:
    def floyd_warshall(self,adj):
        row = len(adj)
        col = len(adj[0])
        for via in range(row):
            for i in range(row):
                for j in range(col):
                    adj[i][j] = min(adj[i][j],adj[i][via]+adj[via][j])
       
    
    def findResult(self,n,spm,distanceThreshold):
        maxResult = -1
        maxCount  =n+1
        for i in range(n):
            count = 0
            for j in range(n):
                if spm[i][j]<=distanceThreshold:
                    count +=1
            if maxCount>=count:
                maxCount = count
                maxResult = i
        return maxResult

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        self.biValue = 10**9+7
        spm = [[self.biValue]*n for i in range(n)]
        for i in range(n):
            spm[i][i]=0
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            spm[u][v]=w
            spm[v][u]=w
        
        self.floyd_warshall(spm)
       
        return self.findResult(n,spm,distanceThreshold)
        
        
