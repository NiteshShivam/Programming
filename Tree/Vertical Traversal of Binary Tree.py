'''
https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1
'''
from collections import deque
class Solution:
    def verticalOrder(self, root): 
        ans = []
        self.level(root,ans)
        #print(ans)
        res = sorted(ans,key=lambda x:x[1])
        #print(res)
        res = [x[0] for x in res]
        return res
        
    
    def level(self,root,ans):
        if not root:
            return []
        que = deque()
        que.append((root,0))
        while que:
            node,col = que.popleft()
            ans.append((node.data,col))
            if node.left:
                que.append((node.left,col-1))
            if node.right:
                que.append((node.right,col+1))
        return ans
