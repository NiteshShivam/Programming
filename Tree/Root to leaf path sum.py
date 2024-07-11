'''
Given a binary tree and an integer target,
check whether there is a root-to-leaf path with its sum as target.


https://www.geeksforgeeks.org/problems/root-to-leaf-path-sum/1
'''
def dfs(root,target):
        if not root:
            if target==0:
                return True
            return False
        if root.left is None and root.right is None:
            if target-root.data==0:
                return True
            return False
        left,right=False,False
        if root.left:
            left = dfs(root.left,target-root.data)
        if root.right:
            right =dfs(root.right,target-root.data)
        return left or right
