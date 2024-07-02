'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def __init__(self):
        self.inorder = None
        self.preorder = None
        self.idx = 0

    def solve(self,start,end):
        if start>end:
            return None
        root = Node(self.preorder[self.idx])
        rootVal = self.preorder[self.idx]
        i = start
        while i<=end:
            if self.inorder[i]==rootVal:
                break
            i+=1
        self.idx = self.idx+1
        root.left = self.solve(start,i-1)
        root.right = self.solve(i+1,end)
        return root
        
    def buildtree(self, inorder, preorder, n):
        self.inorder = inorder
        self.preorder = preorder
        self.idx = 0
        start = 0
        end = n-1
        T = self.solve(start,end)
        return T
