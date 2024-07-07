'''
Given a Binary Tree with all unique values and two nodes value, n1 and n2.
The task is to find the lowest common ancestor of the given two nodes.
We may assume that either both n1 and n2 are present in the tree or none of them are present.

LCA: It is the first common ancestor of both the nodes n1 and n2 from bottom of tree.


https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1
https://youtu.be/Oi3_06ultic
'''

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if not root:
            return root
        if root.data==n1 or root.data==n2:
            return root
        l = self.lca(root.left,n1,n2)
        r = self.lca(root.right,n1,n2)
        if l and r:
            return root
        if l!=None:
            return l
        if r!=None:
            return r
        
