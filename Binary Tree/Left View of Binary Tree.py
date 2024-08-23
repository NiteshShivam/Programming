'''
https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1
'''
from collections import deque
#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    result=[]
    q = deque()
    q.append(root)
    while q:
        length = len(q)
        flag = True
        while length:
            temp = q.popleft()
            if flag:
                flag = not flag
                result.append(temp.data)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            length-=1
    return result
        
