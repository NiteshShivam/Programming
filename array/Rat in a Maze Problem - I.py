#User function Template for python3
'''

https://www.youtube.com/watch?v=wXwZSytYrIs
https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
'''
import math
class Solution:
    def __init__(self):
        self.answer = []
        self.m = 0
    
    def solve(self,i,j,mat,result):
        m = self.m
        n = self.m
        if mat[i][j]==0:
            return
        if i==m-1 and j==n-1:
            self.answer.append(result)
        mat[i][j]=0
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        direct = "ULDR"
        for k in range(4):
            temp = direction[k]
            ci=i+temp[0]
            cj = j+temp[1]
            if ci>=0 and ci<m and  cj>=0 and cj<n:
                if mat[ci][cj]==1:
                    self.solve(ci,cj,mat,result+direct[k])
        mat[i][j]=1
    def findPath(self, mat):
        self.answer = []
        
        self.m = len(mat)
        self.solve(0,0,mat,"")
        return self.answer
