'''
https://www.geeksforgeeks.org/problems/k-pangrams0909/1
'''
class Solution:
    def kPangram(self,string, k):
        s = set()
        count =0
        for each in string:
            if each!=' ':
                s.add(each)
                count +=1
        unique = len(s)
        duplicate = count-unique
        required = 26-unique
        if duplicate>=required and required<=k:
            return True
        return False
