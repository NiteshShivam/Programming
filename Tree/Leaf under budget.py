'''
https://www.geeksforgeeks.org/problems/leaf-under-budget/1
'''


'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
from collections import deque
class Solution:
    def getCount(self,root,n):
        queue = deque()
        count =0
        queue.append(root)
        level =1
        result=0
        while queue and n>0:
            length = len(queue)
            while length:
                q = queue.popleft()
                if not q.left and not q.right:
                    if level+result<=n:
                        count+=1
                        n=n-level
                    else:
                        return count
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
                length-=1
            level+=1
        return count
