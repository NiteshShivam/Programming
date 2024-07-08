'''
Given a binary tree, a target node in the binary tree, and an integer value k, 
find all the nodes that are at distance k from the given target node. No parent pointers are available.
Note:

You have to return the list in sorted order.
The tree will not contain duplicate values.


https://www.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1
https://youtu.be/1PMjfQl_UVQ

'''

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque
class Solution:
    def __init__(self):
        self.parent = {}
        self.result = []
        self.ta = None
        self.target = None
    def inorder(self,root):
        if not root:
            return
        if root.left:
            self.parent[root.left]=root
        self.inorder(root.left)
        if root.data==self.ta:
            self.target = root
        if root.right:
            self.parent[root.right]=root
        self.inorder(root.right)
    def bfs(self,target,k):
        que = deque()
        que.append(target)
        visited = set()
        visited.add(target.data)
        while que:
            length = len(que)
            if k==0:
                #self.result = [node.data for node in que]
                break
            while length:
                temp = que.popleft()
                for neighbour in (temp.left,temp.right,self.parent.get(temp)):
                    if neighbour and neighbour.data not in visited:
                        que.append(neighbour)
                        visited.add(neighbour.data)
                # if temp.left and temp.left.data not in visited:
                #     visited.add(temp.left.data)
                #     que.append(temp.left)
                # if temp.right and temp.right.data not in visited:
                #     visited.add(temp.right.data)
                #     que.append(temp.right)
                    
                # if temp in self.parent and self.parent[temp].data not in visited:
                #     que.append(self.parent[temp])
                #     visited.add(self.parent[temp].data)
                length-=1
            k-=1
        self.result = [node.data for node in que]
            
    def KDistanceNodes(self,root,target,k):
        self.ta=target
        self.inorder(root)
        if self.target:
            self.bfs(self.target,k)
        self.result.sort()
        return self.result
