'''
https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1
'''
class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        if len(str1)<=2:
            return str1==str2
        s1 = str1[2:] + str1[:2]
        if s1==str2:
            return 1
        s1 = str1[-2::]+str1[:-2:]
        
        if s1==str2:
            return 1
       
        return 0
    
