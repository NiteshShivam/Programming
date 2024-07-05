'''
Given an adjacency list of a graph adj of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.
Leetcode :
785. Is Graph Bipartite?
'''
from collections import deque
class Solution:
    def __init__(self):
        self.visited = None
    def dfs(self,u,adj,currentColor):
        self.visited[u]=currentColor
        for v in adj[u]:
            if self.visited[v]==currentColor:
                return False
            if self.visited[v]==-1:
                newColor = 1 -currentColor
                if not self.dfs(v,adj,newColor):
                    return False
        return True
    def bfs(self,u,adj,currentColor):
        queue = deque()
        self.visited[u]=currentColor
        queue.append(u)
        while queue:
            temp = queue.popleft() 
            for v in adj[temp]:
                if self.visited[v]==self.visited[temp]:
                    return False
                elif self.visited[v]==-1:
                    self.visited[v]=1-self.visited[temp]
                    queue.append(v)
        return True
	def isBipartite(self, V, adj):
	    self.visited = [-1]*V
	    '''for i in range(V):
	        if self.visited[i]==-1:
	           if not self.dfs(i,adj,0):
	               return 0'''
	    for i in range(V):
	        if self.visited[i]==-1:
	            if not self.bfs(i,adj,0):
	                return 0
		return 1
