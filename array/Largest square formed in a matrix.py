'''
Given a binary matrix mat of size n * m, 
find out the maximum length of a side of a square sub-matrix with all 1s.

https://www.youtube.com/watch?v=MMr19RE7KYY
'''


from typing import List


class Solution:
    def __init__(self):
        self.mat = None
        self.row = 0
        self.col = 0
        self.result = 0
        self.dp = None
    def solve(self,i,j):
        if i>=self.row or j>=self.col:
            return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        right = self.solve(i,j+1)
        diagonal = self.solve(i+1,j+1)
        down = self.solve(i+1,j)
        if self.mat[i][j]==1:
            self.dp[i][j] = 1 + min(right,diagonal,down)
            self.result = max(self.result, self.dp[i][j])
        else:
            self.dp[i][j]=0
            return 0
        
        return self.dp[i][j]
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
    
        self.mat = mat
        self.row = len(mat)
        self.col = len(mat[0])
        self.dp = [[-1]*self.col for i in range(self.row)]
        self.result = 0
        self.solve(0,0)
        return self.result
