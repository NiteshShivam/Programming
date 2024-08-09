'''
https://www.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1
'''
class Solution:
    def Maximize(self, a): 
        # Complete the function
        a.sort()
        mod = 10**9+7
        length = len(a)
        result = 0
        for i in range(1,length):
            result+= i*a[i]
        return result%mod
