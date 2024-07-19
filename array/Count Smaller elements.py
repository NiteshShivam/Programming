'''
Given an array arr containing non-negative integers. 
Count and return an array ans where ans[i] denotes the number of smaller elements on right side of arr[i].

https://www.geeksforgeeks.org/problems/count-smaller-elements2214/1
'''
#User function Template for python3
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1
class Solution:
	def constructLowerArray(self,arr):
	    def height(root):
            if not root:
                return 0
            return root.height
        def get_size(root):
            if not root:
                return 0
            return root.size
        def max(a,b):
            if a>b:
                return a
            return b
        def right_rotate(root):
            temp1 = root.left
            temp2 = temp1.right
            temp1.right = root
            root.left = temp2
            root.height = max(height(root.left),height(root.right))+1
            temp1.height = max(height(temp1.left),height(temp1.right))+1
            
            root.size = get_size(root.left)+get_size(root.right)+1
            temp1.size = get_size(temp1.left)+get_size(temp1.right)+1
            
            return temp1
        def left_rotate(root):
            temp1 = root.right
            temp2 = temp1.left
            temp1.left = root
            root.right = temp2
            
            root.height = max(height(root.left),height(root.right))+1
            temp1.height = max(height(temp1.left),height(temp1.right))+1
            
            root.size = get_size(root.left)+get_size(root.right)+1
            temp1.size = get_size(temp1.left)+get_size(temp1.right)+1
            
            return temp1
            
        def get_balance(root):
            if not root:
                return 0
            return height(root.left)-height(root.right)
        def insert(root,data,count):
            if not root:
                return Node(data)
            if data<=root.data:
                root.left = insert(root.left,data,count)
            else:
                root.right = insert(root.right,data,count)
                count[0]+=get_size(root.left)+1
            root.height = max(height(root.left),height(root.right))+1
            root.size = get_size(root.left)+get_size(root.right)+1
            balance = get_balance(root)
            if balance>1 and data<root.left.data:
                return right_rotate(root)
                
            if balance<-1 and data>root.right.data:
                return left_rotate(root)
                
            if balance>1 and data>root.left.data:
                root.left = left_rotate(root.left)
                return right_rotate(root)
                
            if balance<-1 and data<root.right.data:
                root.right = right_rotate(root.right)
                return left_rotate(root)
                
            return root
		size = len(arr)
		smaller = [0]*size
		root = None
		for index in range(size-1,-1,-1):
		    count = [0]
		    root = insert(root,arr[index],count)
		    smaller[index]=count[0]
		return smaller
