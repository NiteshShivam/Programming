'''
https://youtu.be/K_LamGUvwUc
https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
'''
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        visited = [0]*V
        currentdfs = [0]*V
        def dfs(i):
            visited[i]=1
            currentdfs[i]=1
            for each in adj[i]:
                if visited[each]==0 and dfs(each):
                    return True
                elif currentdfs[each]==1:
                    return True
            currentdfs[i]=0
            return False
        
        for i in range(V):
            if visited[i]==0 and dfs(i):
                return True
        return False
