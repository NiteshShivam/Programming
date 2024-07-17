'''
Given the root of a Binary Search Tree (BST), 
convert it to a Greater Tree such that every key of the original BST is changed 
to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.



https://www.youtube.com/watch?v=z-pX53sYwWI
https://leetcode.com/problems/delete-nodes-and-return-forest/description/
'''
from collections import deque
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        st = set(to_delete)
        result = []
        def deleteNode(root):
            if not root:
                return None
            root.left = deleteNode(root.left)
            root.right = deleteNode(root.right)
            if root.val in st:
                if root.left:
                    result.append(root.left)
                if root.right:
                    result.append(root.right)
                return None
            else:
                return root

        deleteNode(root)
        if root.val not in st:
            result.append(root)

        return result
