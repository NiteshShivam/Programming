class Solution:
    def __init__(self):
        self.arr = None
        self.direction = None
        self.row=0
        self.col = 0
        self.result = 0
    def dfs(self,i,j,visited):
        if i<0 or i>=self.row or j<0 or j>=self.col:
            return 0
        visited[i][j]=1
        temp=1
        for each in self.direction:
            u = each[0]+i
            v = each[1]+j
            if u>=0 and u<self.row and v>=0 and v<self.col and visited[u][v]==-1 and  self.arr[u][v]==1:
                temp+=self.dfs(u,v,visited)
        return temp
        
    def MaxConnection(self, grid : List[List[int]]) -> int:
        self.arr = grid
        self.direction = [(1,0),(0,1),(-1,0),(0,-1)]
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                visited = [[-1]*self.col for i in range(self.row)]
                self.result = max(self.result,self.dfs(i,j,visited))
        return self.result
                
=============================

from typing import List
class UnionFind:
    def __init__(self,size):
        self.parent = list(range(size))
        self.rank = [1]*size
        self.size = [1]*size
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.parent[rootY]=rootX
                self.size[rootX] +=self.size[rootY]
            elif self.rank[rootX]<self.rank[rootY]:
                self.parent[rootX]=rootY
                self.size[rootY]+=self.size[rootX]
            else:
                self.parent[rootY]=rootX
                self.rank[rootX]=1+self.rank[rootX]
                self.size[rootX]+=self.size[rootY]
            
    def get_size(self,x):
        root = self.find(x)
        return self.size[root]
class Solution:
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n*n)
        def index(x,y):
            return x*n+y
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    for direction in self.directions:
                        ni,nj = i+direction[0],j+direction[1]
                        if 0<=ni<n and 0<=nj<n and grid[ni][nj]==1:
                            uf.union(index(i,j),index(ni,nj))
        max_group_size=0
        component_size_cache = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    root = uf.find(index(i, j))
                    if root not in component_size_cache:
                        component_size_cache[root] = uf.get_size(index(i, j))  # Cache the component size
                    max_group_size = max(max_group_size, component_size_cache[root])
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    seen = set()
                    new_size=1
                    for direction in self.directions:
                        ni,nj = i+direction[0],j+direction[1]
                        if 0<=ni<n and 0<=nj<n and grid[ni][nj]==1:
                            root = uf.find(index(ni,nj))
                            if root not in seen:
                                new_size += component_size_cache[root]
                                seen.add(root)
                    max_group_size=max(max_group_size,new_size)
        return max_group_size
