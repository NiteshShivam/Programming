'''
https://www.youtube.com/watch?v=6GXfmgfOGeQ&t=75s
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
'''

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





===================================
Approach 3:
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(root,s,t):
            if not root:
                return None
            if root.val==s or root.val==t:
                return root
            leftVal = lca(root.left,s,t)
            rightVal = lca(root.right,s,t)
            if leftVal and rightVal:
                return root
            if leftVal:
                return leftVal
            else:
                return rightVal
        commonP = lca(root,startValue,destValue)
        lcaS = ""
        lcaD = ""
        def find(node,s):
            path = []
            def dfs(n):
                if not n:
                    return False
                if n.val == s:
                    return True
                path.append("L")
                if dfs(n.left):
                    return True
                path.pop()
                path.append("R")
                if dfs(n.right):
                    return True
                path.pop()
                return False

            dfs(node)
            return path

        lcaS =find(commonP,startValue)
        lcaD = find(commonP,destValue)
        result = ""
        result += "U"*len(lcaS)
        result += ''.join(lcaD)
        return result
