'''
https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
'''
from collections import deque
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        que = deque()
        unique ={}
        minV = 0
        maxV  = 0
        unique[0]=root.data
        que.append((root,0))
        while que:
            temp = que.popleft()
            node = temp[0]
            dire = temp[1]
            if dire not in unique:
                unique[dire]=node.data
            if node.left:
                minV = min(minV,dire-1)
                que.append((node.left,dire-1))
            if node.right:
                maxV = max(maxV,dire+1)
                que.append((node.right,dire+1))
        result = []
        for i in range(minV,maxV+1):
            if i in unique:
                result.append(unique[i])
        return result
