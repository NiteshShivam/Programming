'''Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j 
such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, 
your task is to find any valid topological sorting of the graph.

In a topological sort, for every directed edge u -> v,  u must come before v in the ordering

'''
# Approach :
from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        indegree = [0]*V
        for u in range(V):
            for v in adj[u]:
                indegree[v]+=1
        q = deque()
        result = []
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                
        while q:
            temp = q.popleft()
            result.append(temp)
            for each in adj[temp]:
                indegree[each]-=1
                if indegree[each]==0:
                    q.append(each)
        return result
        # Code here



Approach 2:
    # adj[v] = each
    # each = (v,weight) ,directed graph
    # link : https://github.com/NiteshShivam/Programming/blob/main/Graph/Shortest%20path%20in%20Directed%20Acyclic%20Graph.py
    # https://www.youtube.com/watch?v=ZUFQfFaU-8U
    def topoSortDFS(self,V,adj):
        stack = []
        visited = [False]*V
        def dfs(v,visited,stack):
            visited[v]=True
            for each in adj[v]:
                temp = each[0]
                if visited[temp]==False:
                    dfs(temp,visited,stack)
            stack.append(v)
        for i in range(V):
            if visited[i]==False:
                dfs(i,visited,stack)
        result = []
        while stack:
            result.append(stack.pop())
        return result
