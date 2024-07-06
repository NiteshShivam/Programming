#User function Template for python3
'''
Given a Binary Tree, complete the function to populate the next pointer for all nodes. 
The next pointer for every node should point to the Inorder successor of the node.
You do not have to return or print anything. Just make changes in the root node given to you.

Note: The node having no in-order successor will be pointed to -1. 
You don't have to add -1 explicitly, the driver code will take care of this.


https://www.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1
'''

class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None


class Solution:
    
    def populateNext(self, root):
        prev = None
        def solve(root):
            nonlocal prev
            if not root:
                return
            solve(root.left)
            if not prev:
                prev=root
            else:
                prev.next=root
                prev=root
            solve(root.right)
        solve(root)
        
    
