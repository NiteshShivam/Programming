'''
https://www.geeksforgeeks.org/problems/sorting-employees5907/1
'''
class Solution:
    def sortRecords(self, a, n):
        a.sort(key=lambda x:(x[1],x[0]))
