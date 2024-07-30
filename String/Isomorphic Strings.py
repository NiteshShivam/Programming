'''

https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1
https://youtu.be/2ISNCDJEgqQ
'''
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        length = len(str1)
        if len(str1)!=len(str2):
            return 0
        hash1 = {}
        hash2 = {}

        for i in range(length):
            fc = str1[i]
            sc = str2[i]
            if fc not in hash1:
                hash1[fc]=sc
            else:
                if hash1[fc]!=sc:
                    return False
            if sc not in hash2:
                hash2[sc]=fc
            else:
                if hash2[sc]!=fc:
                    return False
        return True
