#User function Template for python3
'''
Given inorder and postorder traversals of a binary tree(having n nodes) in
the arrays in[] and post[] respectively. The task is to construct a unique binary tree from these traversals.

Driver code will print the preorder traversal of the constructed tree.

Note :- The inorder and postorder traversals contain unique values, and 
every value present in the postorder traversal is also found in the inorder traversal.


https://www.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1

https://youtu.be/y6zSY_z7Kh4
'''
'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def __init__(self):
        self.In = None
        self.post = None
        self.idx=0
    def solve(self,start,end):
        if start>end:
            return None
        root = Node(self.post[self.idx])
        rootVal = self.post[self.idx]
        i = start
        while i<=end:
            if self.In[i]==rootVal:
                break
            i+=1
        self.idx = self.idx-1
        root.right = self.solve(i+1,end)#first call right subtree
        root.left = self.solve(start,i-1)
        
        return root
            
    def buildTree(self,n , In, post):
        start = 0
        end = n-1
        self.idx = n-1
        self.In = In
        self.post = post
        return self.solve(start,end)
    
