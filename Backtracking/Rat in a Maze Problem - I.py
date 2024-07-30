'''
https://www.youtube.com/watch?v=wXwZSytYrIs
https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
'''

from typing import List
from collections import deque
class Solution:
    
    def solve(self,i,j,s):
        row = len(self.m)
        col = len(self.m[0])
        if self.m[i][j]==0:
            return
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        dire = 'UDLR'
        if i==row-1 and j==col-1:
            self.result.append(s)
        self.m[i][j]=0
        for d in range(4):
            i1 = i+direction[d][0]
            i2 = j+direction[d][1]
            if i1>=0 and i1<row and i2>=0 and i2<col and self.m[i1][i2]==1:
                self.solve(i1,i2,s+dire[d])
        self.m[i][j]=1
    def findPath(self, m: List[List[int]]) -> List[str]:
        self.m = m
        self.result = []
        self.solve(0,0,"")
        
        return self.result
        
