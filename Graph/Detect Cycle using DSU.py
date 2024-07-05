'''Given an undirected graph with no self loops with V (from 0 to V-1) nodes and E edges, 
the task is to check if there is any cycle in the undirected graph.

Note: Solve the problem using disjoint set union (DSU).
'''


class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []
    def Union(self,x,y):
        parentx = self.find(x)
        parenty = self.find(y)
        if parentx==parenty:
            return 
        if self.rank[parentx]>self.rank[parentx]:
            self.parent[parenty]=parentx
        elif self.rank[parentx]<self.rank[parenty]:
            self.parent[parentx]=parenty
        else:
            self.rank[parenty]=self.rank[parenty]+1
            self.parent[parentx]=parenty
        #return False
    def find(self,i):
        if i==self.parent[i]:
            return i
        self.parent[i]=  self.find(self.parent[i])
        return self.parent[i]

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, V, adj):
		#Code here
		self.parent = [i for i in range(V)]
		self.rank = [1]*(V)
		for u in range(V):
		    for v in adj[u]:
		        if u<v:
		            parentu = self.find(u)
		            parentv = self.find(v)
		            if parentu==parentv:
		                return 1
		            self.Union(u,v)
		return 0
