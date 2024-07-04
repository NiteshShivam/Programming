'''You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to
find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.

'''
# Approach :

class Solution:
    def dfs(self,visited,adj,result,root):
        visited[root]=True
        result.append(root)
        for each in adj[root]:
            if visited[each]==False:
                self.dfs(visited,adj,result,each)
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        result = []
        visited = [False]*V
        root = 0
        self.dfs(visited,adj,result,root)
        return result
