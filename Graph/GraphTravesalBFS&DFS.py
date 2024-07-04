from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def __init__(self):
        self.visited=None


    def dfs(self,adj,u,parent):
        self.visited[u]=True
        for each in adj[u]:
            if each==parent:
                continue
            if self.visited[each]==True:
                return True
            if  self.dfs(adj,each,u):
                return True
        return False




    def bfs(self,adj,u):
        self.visited[u]=True
        queue = deque()
        queue.append([u,-1])
        while  queue:
            temp = queue.popleft()
            source = temp[0]
            parent=temp[1]
            for each in adj[source]:
                if each==parent:
                    continue
                if self.visited[each]==True:
                    return True
                self.visited[each]=True
                queue.append([each,source])
        return False




	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		self.visited = [False]*V
		for i in range(V):
		    if not self.visited[i] and self.bfs(adj,i):
		        return True
		return False

