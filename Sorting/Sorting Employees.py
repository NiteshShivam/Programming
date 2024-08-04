'''
https://www.geeksforgeeks.org/problems/sorting-employees5907/1
'''
class Solution:
    def sortRecords(self, a, n):
        a.sort(key=lambda x:(x[1],x[0]))


======================
import functools

class Solution:
    
    def sortRecords(self, a, n):
        def compare(x,y):
            if x[1]<y[1]:
                return -1
            elif x[1]>y[1]:
                return 1
            else:
                if x[0]<y[0]:
                    return -1
                elif x[0]>y[0]:
                    return 1
                else:
                    return 0
        a.sort(key=functools.cmp_to_key(compare))
