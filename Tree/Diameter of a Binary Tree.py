'''
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. 
https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1
https://youtu.be/15KwRECEXLU

'''
class Solution:
    def __init__(self):
        self.result = 0
    def height(self,root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.result = max(self.result,1+left+right)
        return 1+max(left,right)
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        self.result = -1
        self.height(root)
        return self.result
