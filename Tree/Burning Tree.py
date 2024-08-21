'''
https://www.geeksforgeeks.org/problems/burning-tree/1

'''
from collections import deque
class Solution:

    
    def minTime(self, root,target):
        self.map = {}
        self.map[root]=None
        q = deque()
        q.append(root)
        temp = None
        while q:
            node = q.popleft()
            if node.data==target:
                temp=node
            if node.left:
                self.map[node.left]=node
                q.append(node.left)
            if node.right:
                self.map[node.right]=node
                q.append(node.right)
        
        result =0      
        visited = set()
        visited.add(temp)
        q.append(temp)
        while q:
            length = len(q)
            while length:
                node = q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                if node in self.map and self.map[node]!=None and self.map[node] not in visited:
                    q.append(self.map[node])
                    visited.add(self.map[node])
                length-=1
            result+=1
        if result>=1:
            return result-1
        return result
        
