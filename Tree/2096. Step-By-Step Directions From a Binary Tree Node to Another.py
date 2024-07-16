class Solution:
    
    

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(root,search,result):
            if root.val==search:
                return True
            if root.left and dfs(root.left,search,result):
                result.append("L")
            elif root.right and dfs(root.right,search,result):
                result.append("R")
            return result
        sPath = []
        dPath = []
        dfs(root,startValue,sPath)
        dfs(root,destValue,dPath)
        lengthS = len(sPath)
        lengthD = len(dPath)
        s = 0
        d=0
        while s<lengthS and d<lengthD:
            if sPath[-1]==dPath[-1]:
                sPath.pop()
                dPath.pop()
            else:
                break
            s+=1
            d+=1
        t =""
        t+="U"*len(sPath)
        return t + ''.join(reversed(dPath))



Approach 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj = defaultdict(list)
        def inorder(root):
            if not root:
                return
            if root.left:
                adj[root.val].append((root.left.val,"L"))
                adj[root.left.val].append((root.val,"U"))
                inorder(root.left)
            if root.right:
                adj[root.val].append((root.right.val,"R"))
                adj[root.right.val].append((root.val,"U"))
                inorder(root.right)
        inorder(root)
        def bfs(startValue,destValue):
            que = deque()
            visited = set()
            que.append((startValue,""))
            visited.add(startValue)
            while que:
                nodeV,path = que.popleft()
                if nodeV==destValue:
                    return path
                for child,st in adj[nodeV]:
                    if child not in visited:
                        visited.add(child)
                        que.append((child,path+st))
            return ""
        

                        
                        
        return bfs(startValue,destValue)
