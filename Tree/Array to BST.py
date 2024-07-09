'''

Given a sorted array. Convert it into a Height balanced Binary Search Tree (BST). 
Find the preorder traversal of height balanced BST. 
If there exist many such balanced BST consider the tree whose preorder is lexicographically smallest.
Height balanced BST means a binary tree in which the depth of the left subtree and the right subtree of every node never differ by more than 1.



https://www.geeksforgeeks.org/problems/array-to-bst4443/1
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.arr = None
        self.result = []
    def solve(self,left,right):
        if left>right:
            return None
        mid = left+(right-left)//2
        T = Node(self.arr[mid])
        T.left = self.solve(left,mid-1)
        T.right = self.solve(mid+1,right)
        return T
    def preorder(self,T):
        if T:
            self.result.append(T.data)
            self.preorder(T.left)
            self.preorder(T.right)
        
	def sortedArrayToBST(self, nums):
	    # code here
	    self.result = []
	    self.arr = nums
	    T = self.solve(0,len(nums)-1)
	    self.preorder(T)
	    return self.result
	    
