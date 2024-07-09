'''
Given a binary tree, print the bottom view from left to right.


https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

https://www.youtube.com/watch?v=0FtVY6I4pB8
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        bottomStore = {}
        que = deque()
        que.append((root,0))
        bottomStore[0]=root.data
        while que:
            temp = que.popleft()
            node = temp[0]
            level = temp[1]
            #bottomStore[level]=node.data
            if node.left:
                bottomStore[level-1]=node.left.data
                que.append((node.left,level-1))
            if node.right:
                bottomStore[level+1]=node.right.data
                que.append((node.right,level+1))
        result = []
        
        Store = sorted(bottomStore.keys())
        
        for key in Store:
             result.append(bottomStore[key])
        return result
