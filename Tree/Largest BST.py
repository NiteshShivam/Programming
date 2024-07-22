'''
Given a binary tree. Find the size of its largest subtree which is a Binary Search Tree.
Note: Here Size equals the number of nodes in the subtree.



https://youtu.be/X0oXMdtUDwo
https://www.geeksforgeeks.org/problems/largest-bst/1
'''
class NodeValue:
    def __init__(self,minNode,maxNode,maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize
class Solution:
    def solve(self,root):
        if not root:
            return NodeValue(float('inf'),float('-inf'),0)
        left = self.solve(root.left)
        right = self.solve(root.right)
        if left.maxNode<root.data and root.data<right.minNode:
            return NodeValue(min(root.data,left.minNode),max(root.data,right.maxNode),left.maxSize+right.maxSize+1)
        return NodeValue(float('-inf'),float('inf'),max(left.maxSize,right.maxSize))
    def largestBst(self, root):
        node = self.solve(root)
        return node.maxSize
