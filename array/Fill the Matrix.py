'''
https://www.geeksforgeeks.org/problems/fill-the-matrix--170647/1
Solution comment:
https://discuss.geeksforgeeks.org/comment/972691000323882a407568fd569bbe5b/practice
'''
class Solution:
    def minIteration(self, N, M, x, y):
       
        top = x-1
        down = N-x
        left = y-1
        right = M-y
        
        return max(top+left,top+right,left+down,down+right)


========================
from collections import deque
class Solution:
    def minIteration(self, N, M, x, y):
        queue = deque()
        queue.append((x-1,y-1))
        matrix = [[0]*M for i in range(N)]
        matrix[x-1][y-1]=1
        direction = [(-1,0),(0,-1),(1,0),(0,1)]
        count=0
        while queue:
            length = len(queue)
            flag=0
            while length>0:
                q = queue.popleft()
                i,j = q
                for each in direction:
                    i1 = each[0]+i
                    j1 = each[1]+j
                    if i1>=0 and i1<N and j1>=0 and j1<M and matrix[i1][j1]==0:
                        queue.append((i1,j1))
                        matrix[i1][j1]=1
                        flag=1
                length-=1
            if flag:
                count+=1
        return count
