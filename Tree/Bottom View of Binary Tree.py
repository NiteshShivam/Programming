'''
Given a binary tree, print the bottom view from left to right.


https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

https://www.youtube.com/watch?v=0FtVY6I4pB8
'''
# without sorting the key ,using min and max function,O(n)
def bottomView(self, root):
        q = deque()
        space = {}
        q.append((root,0))
        while q:
            node,dist = q.popleft()
            if dist not in space:
                space[dist]=node.data
            else:
                space[dist] = node.data
            if node.left:
                q.append((node.left,dist-1))
            if node.right:
                q.append((node.right,dist+1))
        result = [space[key] for key in range(min(space),max(space)+1)]
        return result


==================================
from collections import deque
class Solution:
    def bottomView(self, root):
        bottomStore = {}
        que = deque()
        que.append((root,0))
        bottomStore[0]=root.data
        while que:
            temp = que.popleft()
            node = temp[0]
            level = temp[1]
            #bottomStore[level]=node.data
            if node.left:
                bottomStore[level-1]=node.left.data
                que.append((node.left,level-1))
            if node.right:
                bottomStore[level+1]=node.right.data
                que.append((node.right,level+1))
        result = []
        
        Store = sorted(bottomStore.keys())
        
        for key in Store:
             result.append(bottomStore[key])
        return result
