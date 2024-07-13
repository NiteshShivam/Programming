'''
Given a binary tree and the task is to find the spiral order traversal of the tree.

Spiral order Traversal mean: Starting from level 0 for root node, 
for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right. 


https://www.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1
''''



'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        
from collections import deque
def findSpiral(root):
    stack = deque()
    result = []
    stack.append(root)
    odd=1
    while stack:
        length =len(stack)
        tempS = deque()
        while length:
            temp =  stack.pop()
            result.append(temp.data)
            if odd==1:
                if temp.right:
                    tempS.append(temp.right)
                if temp.left:
                    tempS.append(temp.left)
            else:
                if temp.left:
                    tempS.append(temp.left)
                if temp.right:
                    tempS.append(temp.right)
            length-=1
        stack=tempS
        odd=1-odd
            
