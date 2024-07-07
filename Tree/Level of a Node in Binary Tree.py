'''
Given a Binary Tree and a target key you need to find the level of target key in the given Binary Tree.

Note: The level of the root node is 1.

https://www.geeksforgeeks.org/problems/level-of-a-node-in-binary-tree/1
'''

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def __init__(self):
        self.result = 0
    def dfs(self,root,level,target):
        if not root:
            return
        if root.data == target:
            self.result=level
            return
        self.dfs(root.left,level+1,target)
        self.dfs(root.right,level+1,target)
    def getLevel(self, root,target):
        if not root:
            return -1
        self.dfs(root,1,target)
        return self.result
