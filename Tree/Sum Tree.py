'''
Given a Binary Tree. Return true if, for every node X in the tree other than the leaves, 
its value is equal to the sum of its left subtree's value and its right subtree's value. Else return false.

An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.
'''
class Solution:
    def isSumTree(self,root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        leftSum = self.isSumTree(root.left)
        rightSum = self.isSumTree(root.right)
        if leftSum and rightSum:
            leftVa =0
            rightVa = 0
            if root.left:
                leftVa = root.left.data
            if root.right:
                rightVa = root.right.data
            if root.data==leftVa+rightVa:
                root.data = root.data+leftVa+rightVa
                return True
            else:
                return False
        else:
            return False

===================================================
class Solution:
    def solve(self,root):
        if not root:
            return True,0
        if not root.left and not root.right:
            return True,root.data
        lbool,lvalue =  self.solve(root.left)
        rbool,rvalue = self.solve(root.right)
        if lbool==False or rbool==False:
            return False,0
        if root.data ==lvalue+rvalue:
            return True,root.data+lvalue+rvalue
        else:
            return False,0
    def is_sum_tree(self, node):
        boolB ,v = self.solve(root)
        return boolB
