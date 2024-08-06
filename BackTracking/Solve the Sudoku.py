'''
https://youtu.be/8lWxaRviJBA
https://www.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1
'''

class Solution:
    def isSafe(self,row,col,grid,k):
        for i in range(9):
            if grid[row][i]==k:
                return False
            if grid[i][col]==k:
                return False
       
            
        row = (row//3)*3
        col =(col//3)*3
        for i in range(row,row+3):
            for j in range(col,col+3):
                if grid[i][j]==k:
                    return False
        return True
            
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col]==0:
                    for k in range(1,10):
                        if self.isSafe(row,col,grid,k):
                            grid[row][col]=k
                            result = self.SolveSudoku(grid)
                            if result:
                                return True
                            else:
                                grid[row][col]=0
                    return False
        return True
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")
