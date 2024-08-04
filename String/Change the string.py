'''
https://www.geeksforgeeks.org/problems/change-the-string3541/1
'''
class Solution:
    def modify(self, S):
        if not S:
            return S
        if S[0].isupper():
            return S.upper()
        else:
            return S.lower()
