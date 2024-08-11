'''
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/
https://youtu.be/HCHpyAk1Ekw
'''
class Solution:
    def dfs(self,i,j,matrix,visited):
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        # matrix[i][j]=0
        visited[i][j]=True
        for each in direction:
            new_i = i + each[0]
            new_j = j + each[1]
            if new_i>=0 and new_i<self.row and new_j>=0 and new_j<self.col and matrix[new_i][new_j]==1 and visited[new_i][new_j]==False:
                # matrix[new_i][new_j]=0
                visited[new_i][new_j]=True
                self.dfs(new_i,new_j,matrix,visited)
    def useDfs(self,grid):
        count = 0
        visited = [[False]*self.col for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]==1 and not visited[i][j]:
                    self.dfs(i,j,grid,visited)
                    count+=1
        return count
    def minDays(self, grid: List[List[int]]) -> int:
        
        self.row = len(grid)
        self.col = len(grid[0])
        ans = self.useDfs(grid)
        if ans>1 or ans ==0:
            return 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]==1:
                    grid[i][j]=0
                    count = self.useDfs(grid)
                    if count>1 or count==0:
                        return 1
                    grid[i][j]=1
        return 2
