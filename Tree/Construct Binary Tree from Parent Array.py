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



Approach 2:

===================================================
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        space = {}
        n = len(parent)
        root = None
        for i in range(n):
            par = parent[i]
            if i not in space:
                space[i] = Node(i)
            if par==-1:
                root = space[i]
                continue
            if par not in space:
                space[par] = Node(par)
            if space[par].left  ==None:
                space[par].left=space[i]
            else:
                space[par].right = space[i]
        return root
