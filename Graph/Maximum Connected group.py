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
                
