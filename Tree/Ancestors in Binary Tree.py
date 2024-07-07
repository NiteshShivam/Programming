'''
Given a Binary Tree and an integer target. Find all the ancestors of the given target.

Note:

The ancestor of node x is node y, which is at the upper level of node x,
and x is directly connected with node y. Consider multiple levels of ancestors to solve this problem.
In case there are no ancestors available, return an empty list.

https://www.geeksforgeeks.org/problems/ancestors-in-binary-tree/1
'''
class Solution:
    def __init__(self):
        self.stack = []
    def dfs(self,root,target):
        if not root:
            return False
        if root.data==target:
            return True
        if self.dfs(root.left,target):
            self.stack.append(root.data)
            return True
        if self.dfs(root.right,target):
            self.stack.append(root.data)
            return True
        return False
        

    def Ancestors(self, root, target):
        self.stack = []
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        #code here
        
        self.dfs(root,target)
        return self.stack
