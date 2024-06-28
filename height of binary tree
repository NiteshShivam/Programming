class Solution:
    #Function to find the height of a binary tree.
    def traversal(self,root):
        if not root:
            return 0
        return 1+max(self.traversal(root.left),self.traversal(root.right))
    def height(self, root):
        # code here
        if not root:
            return 0
        t = self.traversal(root.left)
        r = self.traversal(root.right)
        return 1 + max(t,r)
