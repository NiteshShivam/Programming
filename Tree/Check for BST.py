'''
https://www.geeksforgeeks.org/problems/check-for-bst/1
'''
class Solution:
    def check(self,root,lval,rval):
        if not(root.data>lval and root.data<rval):
            return False
        lleft = True
        rright = True
        if root.left:
            lleft = self.check(root.left,lval,root.data)
        if root.right:
            rright = self.check(root.right,root.data,rval)
        return lleft and rright
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        lleft = True
        rright = True
        minV = float('-inf')
        maxV = float('inf')
        if not root:
            return True
        if root.left:
            lleft = self.check(root.left,minV,root.data)
        if root.right:
            rright = self.check(root.right,root.data,maxV)
        
        return lleft and rright
        
