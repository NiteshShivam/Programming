'''

https://youtu.be/M8WnAIhTjmQ
https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/
'''
class Solution:
    def floydWarshall(self,matrix):
        row = len(matrix)
        for via in range(row):
            for i in range(row):
                for j in range(row):
                    matrix[i][j] = min(matrix[i][j],matrix[i][via]+matrix[via][j])

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        length = len(original)
        maxV = float('inf')
        matrix = [[maxV]*26 for i in range(26)]
        for i in range(length):
            s = ord(original[i])-ord('a')
            d = ord(changed[i])-ord('a')
            matrix[s][d]=min(matrix[s][d],cost[i])
        self.floydWarshall(matrix)
        result = 0
        for i in range(len(source)):
            if source[i]!=target[i]:
                s = ord(source[i])-ord('a')
                d = ord(target[i])-ord('a')
                if matrix[s][d]==maxV:
                    return -1
                result = result+matrix[s][d]

        return result        





=====================================
import heapq
class Solution:
    def dijkstra(self,source,adj,distance):
        distance[source]=0
        heap = []
        heapq.heappush(heap,(0,source))
        while heap:
            temp = heapq.heappop(heap)
            cost = temp[0]
            node = temp[1]
            for each in adj[node]:
                w = each[0]
                v = each[1]
                if distance[node]+w<distance[v]:
                    distance[v] = distance[node]+w
                    heapq.heappush(heap,(distance[node]+w,v))

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        length = len(original)
        adj = [[] for _ in range(26)]
        for i in range(length):
            s = ord(original[i])-ord('a')
            d = ord(changed[i])-ord('a')
            adj[s].append((cost[i],d))
        maxV = float('inf')
        matrix = [[maxV]*26 for i in range(26)]
        
        for i in range(len(source)):
            s = ord(source[i])-ord('a')
            self.dijkstra(s,adj,matrix[s])
        result = 0
        for i in range(len(source)):
            if source[i]!=target[i]:
                s = ord(source[i])-ord('a')
                d = ord(target[i])-ord('a')
                if matrix[s][d]==maxV:
                    return -1
                result = result+matrix[s][d]

        return result        
