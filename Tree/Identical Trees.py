#User function Template for python3
'''
Given two binary trees, the task is to find if both of them are identical or not.
Note: You need to return true or false, the printing is done by the driver code.


https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
'''


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.data==root2.data:
            return self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)
        else:
            return False
