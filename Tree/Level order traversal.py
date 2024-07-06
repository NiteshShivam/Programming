
'''
Given a root of a binary tree with n nodes, find its level order traversal.
Level order traversal of a tree is breadth-first traversal for the tree.


https://www.geeksforgeeks.org/problems/level-order-traversal/1
'''
from collections import deque
class Solution:
    def __init(self):
        self.result = []
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        self.result = []
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            while length:
                length-=1
                temp = q.popleft()
                self.result.append(temp.data)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return self.result
