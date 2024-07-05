'''
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) edges[ ][ ] of 
length M, where there is a directed edge from edge[i][0] to edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from src(0) vertex to all the vertices and
if it is impossible to reach any vertex, then return -1 for that vertex.

link : 
https://www.youtube.com/watch?v=ZUFQfFaU-8U
'''
#User function Template for python3
from collections import deque
from typing import List
import sys
class Solution:
    def topoSortBFS(self,V,adj):
        indegree = [0]*V
        for i in range(V):
            for each in adj[i]:
                temp = each[0]
                indegree[temp]+=1
        queue = deque()
        result = []
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            temp = queue.popleft()
            result.append(temp)
            for each in adj[temp]:
                temp1 = each[0]
                indegree[temp1]-=1
                if indegree[temp1]==0:
                    queue.append(temp1)
        return result
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
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        pass
        adj = [[] for i in range(n)]
        for each in edges:
            u = each[0]
            v = each[1]
            w = each[2]
            adj[u].append((v,w))
        #result = self.topoSortBFS(n,adj)
        result  = self.topoSortDFS(n,adj)
        distance = [sys.maxsize]*n
        distance[0]=0
        for i in range(n):
            node = result[i]
            for each in adj[node]:
                v = each[0]
                w = each[1]
                if distance[node]+w<distance[v]:
                    distance[v]=distance[node]+w
        for i in range(n):
            if distance[i]==sys.maxsize:
                distance[i]=-1
        return distance
