'''
https://www.geeksforgeeks.org/problems/zigzag-tree-traversal/1
'''
from collections import deque
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        odd =1
        stack1 = deque()
        stack2 = deque()
        stack1.append(root)
        result = []
        while stack1 or stack2:
            if odd:
                length = len(stack1)
                while length:
                    top = stack1.pop()
                    result.append(top.data)
                    
                    if top.left:
                        stack2.append(top.left)
                    if top.right:
                        stack2.append(top.right)
                        
                    length-=1
            else:
                length = len(stack2)
                while length:
                    top = stack2.pop()
                    result.append(top.data)
                    
                    if top.right:
                        stack1.append(top.right)
                    if top.left:
                        stack1.append(top.left)
                    
                        
                    length-=1
            odd = not odd
        return result
