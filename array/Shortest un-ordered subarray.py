'''
https://www.geeksforgeeks.org/problems/shortest-un-ordered-subarray3634/1
'''
class Solution:
    def shortestUnorderedSubarray(self, a, n):
        for i in range(n):
            a[i] = int(a[i])
        for i in range(n-2):
            if a[i]>a[i+1] and a[i+2]>a[i+1]:
                #print("first",a[i],a[i+1],a[i+2])
                return 3
            if a[i]<a[i+1] and a[i+1]>a[i+2]:
                #print(a[i],a[i+1],a[i+2])
                return 3
        return 0
