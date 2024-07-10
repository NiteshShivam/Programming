'''

Given a Binary Tree of size N , where each node can have positive or negative values.
Convert this to a tree where value of each node will be the sum of the values of all 
the nodes in left and right sub trees of the original tree. The values of leaf nodes are changed to 0.
Note: You have to modify the given tree in-place.



https://www.geeksforgeeks.org/problems/transform-to-sum-tree--170645/1
'''
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def solve(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            temp = root.data
            root.data=0
            return temp
        left = self.solve(root.left)
        right = self.solve(root.right)
        temp = root.data
        root.data = left + right
        return root.data+temp
    def toSumTree(self, root) :
        self.solve(root)
        
        return root
