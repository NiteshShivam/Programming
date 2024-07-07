'''
Given a binary tree having n nodes and an integer k. 
Print all nodes that are at distance k from the root (root is considered at distance 0 from itself).
Nodes should be printed from left to right.

https://www.geeksforgeeks.org/problems/k-distance-from-root/1
'''
'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def __init__(self):
        self.result = []
    def KDistance(self,root,k):
        if k<0 or not root:
            return
        
        if root and k==0:
            self.result.append(root.data)
        self.KDistance(root.left,k-1)
        self.KDistance(root.right,k-1)
        return self.result
    # code here
