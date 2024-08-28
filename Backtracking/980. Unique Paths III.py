'''
https://leetcode.com/problems/unique-paths-iii/description/

mik -video
https://youtu.be/eagGLroZXMk?list=PLpIkg8OmuX-KJPC18SGiRUzJQAYo839ox

'''
class Solution:
    def solve(self,grid,i,j,count):
        if i<0 or i>=self.m or j<0 or j>=self.n or grid[i][j]==-1:
            return 
        
        if grid[i][j]==2:
            if count==self.nObj:
                self.result +=1
            return
        if grid[i][j]==1 or grid[i][j]==0:
            count+=1
        grid[i][j]=-1
        for each in self.direction:
            new_i = i+each[0]
            new_j = j+each[1]
            self.solve(grid,new_i,new_j,count)
        grid[i][j]=0
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.nObj = 0
        self.result = 0
        self.direction = [(-1,0),(1,0),(0,-1),(0,1)]
        self.m = len(grid)
        self.n = len(grid[0])
        startI = 0
        startJ = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]==1 or grid[i][j]==0:
                    self.nObj+=1
                if grid[i][j]==1:
                    startI = i
                    startJ = j
        self.solve(grid,startI,startJ,0)
        
        return self.result
        
