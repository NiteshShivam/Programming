'''
https://leetcode.com/problems/magic-squares-in-grid/description/
'''
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])
        def isGrid(i,j):
            row1,row2,row3,col1,col2,col3,d1,d2=0,0,0,0,0,0,0,0
            unique = set()
            if grid[i+1][j+1]!=5:
                return False
            for k in range(3):
                for t in range(3):
                    if grid[i+k][t+j] in unique or grid[i+k][t+j]>9 or grid[i+k][t+j]<=0:
                        return False
                    else:
                        unique.add(grid[i+k][t+j])
            for k in range(3):
                row1 += grid[i][k+j]
            for k in range(3):
                row2 += grid[i+1][k+j]
            if row1!=row2:
                return False
            for k in range(3):
                row3 += grid[i+2][k+j]
            if row3!=row1:
                return False

            # col
            for k in range(3):
                col1 += grid[i+k][j]
            if row1!=col1:
                return False
            for k in range(3):
                col2 += grid[i+k][j+1]
            if row1!=col2:
                return False
            for k in range(3):
                col3 += grid[i+k][j+2]
            if row1!=col3:
                return False
            
            # diagonal
            for k in range(3):
                d1+= grid[i+k][j+k]
            if d1!=row1:
                return False
            r1=0
            c1 = 2
            for k in range(3):
                d2+=grid[i+r1][j+c1]
                r1+=1
                c1-=1
            if d2!=row1:
                return False

            return True

        for i in range(row-2):
            for j in range(col-2):
                if isGrid(i,j):
                    result+=1

        return result
