'''

https://www.youtube.com/watch?v=QyrmIu4Vo8A
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




==========================
Approach 2:
from collections import defaultdict,deque

class Solution:
    # def dfs(self,i,visited,adj,cycle,stack):
    #     visited[i]=1
    #     for v in adj[i]:
    #         if visited[v]==0:
    #             self.dfs(v,visited,adj,cycle,stack)
    #         elif visited[v]==1:
    #             cycle = True
    #             return
    #     visited[i]=2
    #     stack.append(i)
            

    def dfsSort(self,arr,k):
        adj = defaultdict(list)
        for each in arr:
            u,v = each[0],each[1]
            adj[u].append(v)
        visited = [0]*(k+1)
        stack = deque()
        result = []
        self.cycle=False
        def dfs(i,visited,cycle,stack):
            visited[i]=1
            for v in adj[i]:
                if visited[v]==0:
                    dfs(v,visited,cycle,stack)
                elif visited[v]==1:
                    self.cycle = True
                    return
            visited[i]=2
            stack.append(i)
            
        for i in range(1,k+1):
            if visited[i]==0:
                dfs(i,visited,cycle,stack)
                if self.cycle==True:
                    return []
        while stack:
            result.append(stack.pop())
        return result

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
        # rowResult = self.topoSort(rowConditions,k)
        # colResult = self.topoSort(colConditions,k)
        rowResult = self.dfsSort(rowConditions,k)
        colResult = self.dfsSort(colConditions,k)
        if len(rowResult) ==0 or len(colResult)==0:
            return []
        matrix = [[0]*k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if rowResult[i]==colResult[j]:
                    matrix[i][j]=rowResult[i]
        return matrix
        
