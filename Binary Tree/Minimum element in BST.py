'''
https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1
'''
class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        
        if root.left:
            return self.minValue(root.left)
        else:
            return root.data
