'''
https://leetcode.com/problems/build-a-matrix-with-conditions/description/
'''
from collections import defaultdict,deque

class Solution:
    def topoSort(self,arr,k):
        adj = defaultdict(list)
        indegree = [0]*(k+1)
        for each in arr:
            u,v = each
            adj[u].append(v)
            indegree[v] += 1
        queue = deque()
        result = []
        for i in range(1,k+1):
            if indegree[i]==0:
                queue.append(i)
        count = 0
        while queue:
            q = queue.popleft()
            count+=1
            result.append(q)
            for v in adj[q]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        if count!=k:
            return [] 
        return result
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowResult = self.topoSort(rowConditions,k)
        colResult = self.topoSort(colConditions,k)
        if len(rowResult) ==0 or len(colResult)==0:
            return []
        matrix = [[0]*k for _ in range(k)]
        posR = [0]*(k+1)
        posC = [0]*(k+1)
        for i in range(k):
            posR[rowResult[i]]=i
        for i in range(k):
            posC[colResult[i]]=i
        for i in range(1,k+1):
            matrix[posR[i]][posC[i]]=i
        return matrix
        
