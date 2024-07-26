'''

https://www.youtube.com/watch?v=yYKGNW6Y7BA
https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1
'''


#BFS
from collections import deque
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def bfs(self,i,j,grid):
        direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        queue.append((i,j))
        grid[i][j]=0
        while queue:
            current = queue.popleft()
            u = current[0]
            v=current[1]
            for each in direction:
                i1 = each[0]+u
                j1 = each[1]+v
                if i1>=0 and i1<row and j1>=0 and j1<col and grid[i1][j1]==1:
                    queue.append((i1,j1))
                    grid[i1][j1]=0
    def numIslands(self,grid):
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    self.bfs(i,j,grid)
                    count+=1
        return count


DFS
====================================================
#User function Template for python3
from collections import deque
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self,i,j,grid):
        grid[i][j]=0
        direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for each in direction:
            i1 = each[0]+i
            j1 = each[1]+j
            if i1>=0 and i1<row and j1>=0 and j1<col and grid[i1][j1]==1:
                self.dfs(i1,j1,grid)
    def bfs(self,i,j,grid):
        direction = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        queue.append((i,j))
        grid[i][j]=0
        while queue:
            current = queue.popleft()
            u = current[0]
            v=current[1]
            for each in direction:
                i1 = each[0]+u
                j1 = each[1]+v
                if i1>=0 and i1<row and j1>=0 and j1<col and grid[i1][j1]==1:
                    queue.append((i1,j1))
                    grid[i1][j1]=0
    def numIslands(self,grid):
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    self.bfs(i,j,grid)
                    count+=1
        return count
        

