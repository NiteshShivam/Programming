'''
Given a binary tree (having distinct node values) and two node values. 
Check whether the two node values are cousins of each other or not.
Note: Two nodes of a binary tree are cousins if they have the same depth with different parents.

https://www.geeksforgeeks.org/problems/check-if-two-nodes-are-cousins/1

'''
'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
from collections import deque
# Returns true if the nodes with values 'a' and 'b' are cousins. Else returns false
def isCousin(root, a, b):
    # Your code here
    aParent = None
    bParent = None
    alevel = 0
    blevel = 0
    queue = deque()
    level = 0
    queue.append(root)
    if root.data==a:
        alevel = 0
    if root.data==b:
        blevel=0
    while queue:
        length = len(queue)
        while length:
            temp = queue.popleft()
            if temp.left:
                if temp.left.data==a:
                    aParent=temp
                    alevel = level
                if temp.left.data==b:
                    bParent=temp
                    blevel = level
                queue.append(temp.left)
            if temp.right:
                if temp.right.data==a:
                    aParent=temp
                    alevel = level
                if temp.right.data==b:
                    bParent=temp
                    blevel = level
                queue.append(temp.right)
            length-=1
        level+=1
    if aParent==None or bParent==None:
        return False
    if alevel==blevel and aParent!=bParent:
        return True
        
    return False
