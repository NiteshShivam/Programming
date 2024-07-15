'''
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] 
indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid




https://leetcode.com/problems/create-binary-tree-from-descriptions/description/
'''
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        store = {}
        childSet = set()
        for each in descriptions:
            p = each[0]
            c = each[1]
            l = each[2]
            childSet.add(c)
            parentNode = None
            childNode = None
            if p in store:
                parentNode = store[p]
            else:
                parentNode = TreeNode(p)
                store[p]=parentNode
            
            if c in store:
                childNode = store[c]
            else:
                childNode = TreeNode(c)
                store[c]=childNode
            
            if l==1:
                parentNode.left=childNode
                
            else:
                parentNode.right = childNode

        for key,value in store.items():
            if key not in childSet:
                return value
