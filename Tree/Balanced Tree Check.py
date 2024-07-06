
'''
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1
'''
'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def __init__(self):
        self.valid = True
    def heigth(self,root):
        if not root:
            return 0
        l = self.heigth(root.left)
        r = self.heigth(root.right)
        if abs(l-r)>1:
            self.valid =False
        return 1 + max(l,r)
            
    def isBalanced(self,root):
        self.heigth(root)
        return self.valid
        #add code here
