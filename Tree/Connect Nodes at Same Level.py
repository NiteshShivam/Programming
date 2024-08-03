'''
https://www.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
'''
import sys
sys.setrecursionlimit(50000)
# Tree Node
from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        if not root:
            return
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            prev = None
            while length:
                p = queue.popleft()
                if prev:
                    prev.nextRight = p
                prev = p
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                
                length-=1






=======================
#User function Template for python3

import sys
sys.setrecursionlimit(50000)
# Tree Node
from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            while length > 1:
                p = queue.popleft()
                p.nextRight = queue[0]
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                length -= 1
            q =queue.popleft()
            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)
