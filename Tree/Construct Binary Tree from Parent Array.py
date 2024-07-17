'''
https://www.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/1
'''
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        space = {}
        n = len(parent)
        root = None
        for i in range(n):
            t = Node(i)
            space[i]=t
            if parent[i]==-1:
                root=t
        for i in range(n):
            value = parent[i]
            if value!=-1:
                node = space[value]
                if space[value].left is None:
                    space[value].left = space[i]
                else:
                    space[value].right = space[i]
        return root
