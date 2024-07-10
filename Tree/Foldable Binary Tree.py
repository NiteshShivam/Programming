'''

Given a binary tree, check if the tree can be folded or not. 
A tree can be folded if left and right subtrees of the tree are structure wise mirror image of each other.
An empty tree is considered as foldable.


https://www.geeksforgeeks.org/problems/foldable-binary-tree/1
'''

'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

'''
def solve(left,right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return solve(left.right,right.left) and solve(left.left,right.right)
def IsFoldable(root):
    if not root:
        return True
    return solve(root.left,root.right)
