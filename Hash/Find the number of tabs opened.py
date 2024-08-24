'''
https://www.geeksforgeeks.org/problems/tiger-zinda-hai5531/1
'''

class Solution:
    def countTabs(self, arr):
        s = set()
        for each in arr:
            if each=='END':
                s.clear()
            elif each in s:
                s.remove(each)
            else:
                s.add(each)
        return len(s)
