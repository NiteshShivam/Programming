'''
Given two binary trees with head reference as T and S having at most N nodes. 
The task is to check if S is present as subtree in T.
A subtree of a tree T1 is a tree T2 consisting of a node in T1 and all of its descendants in T1.


https://www.geeksforgeeks.org/problems/check-if-subtree/1
'''
class Solution:
    def solve(self,T,S):
        if not T and not S:
            return True
        if not T or not S:
            return False
        if T.data==S.data:
            return self.solve(T.left,S.left) and self.solve(T.right,S.right)
    def isSubTree(self, T, S):
        if not S:
            return True
        if not T:
            return False
        if self.solve(T,S):
            return True
        return self.isSubTree(T.left,S) or self.isSubTree(T.right,S)
