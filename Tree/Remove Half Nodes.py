'''
You are given a binary tree and you need to remove all the half nodes (which have only one child). 
Return the root node of the modified tree after removing all the half-nodes.


Note: The output will be judged by the inorder traversal of the resultant tree, inside the driver code.
'''
class Solution:
    def dfs(self,root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)
        if root.left and not root.right:
            return root.left
        if not root.left and root.right:
            return root.right
        return root
    def RemoveHalfNodes(self, node):
        root = self.dfs(node)
        return root
