'''
Given a string, s, the objective is to convert it into integer format without 
utilizing any built-in functions. If the conversion is not feasible, the function should return -1.

Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.

https://www.geeksforgeeks.org/problems/implement-atoi/1
'''
class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        length = len(s)
        if length:
            if not (s[0]=='-' or s[0].isdigit()):
                return -1
        
        for i in range(1,length):
            if s[i].isdigit():
                continue
            else:
                return -1
        return int(s)
