'''
Given a string s consisting of lowercase Latin Letters. 
Return the first non-repeating character in s. If there is no non-repeating character, return '$'.

Note : When you return '$' driver code will output -1.


https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1
'''
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        hasM = {}
        for c in s:
            hasM[c]=hasM.get(c,0)+1
        for c in s:
            if hasM[c]==1:
                return c
        return '$'
    
