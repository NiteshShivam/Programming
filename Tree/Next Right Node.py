
'''

Given a Binary tree and a key in the binary tree, 
find the node right to the given key. If there is no node on right side, then return a node with value -1.

https://www.geeksforgeeks.org/problems/next-right-node/1
'''
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
from collections import deque
class Solution:
    def nextRight(self, root, key):
        #code here
        
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            valid = False
            while length:
                temp = q.popleft()
                if valid:
                    return temp
                if temp.data==key:
                    valid = True
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                
                    
                length-=1
            valid = False
        return Node(-1)
