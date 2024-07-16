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
