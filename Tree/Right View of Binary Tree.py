'''
https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1
'''
from queue import Queue
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        result = []
        q = Queue()
        q.put(root)
        while not q.empty():
            length = q.qsize()
            while length:
                temp = q.get()
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
                length-=1
                if length==0:
                    result.append(temp.data)
        return result
