'''
https://discuss.geeksforgeeks.org/comment/09dd9e61012e450b90c6db78f958d44a/practice

https://www.geeksforgeeks.org/problems/finding-profession3834/1
'''
from collections import deque
class Solution:
    def profession(self, level, pos):
        # code here
        if level==1 or pos==1:
            return "e"
        parent = (pos+1)//2
        c = self.profession(level-1,parent)
        if pos ==2*parent-1:
            return c
        else:
            if c=='e':
                return 'd'
            return 'e'
