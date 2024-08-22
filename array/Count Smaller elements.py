'''
Given an array arr containing non-negative integers. 
Count and return an array ans where ans[i] denotes the number of smaller elements on right side of arr[i].

https://www.geeksforgeeks.org/problems/count-smaller-elements2214/1
'''

#Approach 1 : AVL Tree
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

============================
Approach 2: 
class Solution:
    def binarySearch(self,arr,target):
        low = 0
        high = len(arr)
        while low<high:
            mid = low+(high-low)//2
            if arr[mid]<target:
                low = mid+1
            else:
                high = mid
        return low

	def constructLowerArray(self,arr):
		# code here
		length = len(arr)
		result = [0]*length
		sorted_arr = []
		for i in range(length-1,-1,-1):
		    val = arr[i]
		    index = self.binarySearch(sorted_arr,val)
		    result[i]=index
		    sorted_arr.insert(index,val)
		return result


===========================
class Solution:
    def merge(self,left,mid,right,arr,count):
        n = right-left+1
        temp = [None]*n
        i = left
        j = mid+1
        k = 0
        while i<=mid and j<=right:
            if arr[i][0]<=arr[j][0]:
                temp[k] = arr[j]
                k+=1
                j+=1
            else:
                count[arr[i][1]] +=right-j+1
                temp[k] = arr[i]
                k+=1
                i+=1
            
        while i<=mid:
            temp[k] = arr[i]
            k+=1
            i+=1
        while j<=right:
            temp[k] = arr[j]
            k+=1
            j+=1
            
        for i in range(n):
            arr[left+i]=temp[i]
    def mergeSort(self,start,end,arr,count):
        if start<end:
            mid = start+(end-start)//2
            self.mergeSort(start,mid,arr,count)
            self.mergeSort(mid+1,end,arr,count)
            self.merge(start,mid,end,arr,count)
    def constructLowerArray(self,a):
        length = len(a)
        v = []
        for i in range(length):
            v.append((a[i],i))
        count = [0]*length
        self.mergeSort(0,length-1,v,count)
        return count



