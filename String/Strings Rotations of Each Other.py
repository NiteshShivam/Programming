'''
https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1
'''
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        if len(s1)!=len(s2):
            return False
       
        if s2 in 2*s1:
            return True
        return False
