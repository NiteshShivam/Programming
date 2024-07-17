'''
Given an array arr of size n and an integer x. 
Find if there's a triplet in the array which sums up to the given integer x.


https://youtu.be/o9MLd-eLZuQ
https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1
'''

class Solution:
     
    # Should return true if there exists a triplet in the
    # array arr[] which sums to x. Otherwise false
    def find3Numbers(self, arr, n, x):
        arr.sort()
        for i in range(n):
            j = i+1
            k =n-1
            while j<k:
                temp = arr[i]+arr[j]+arr[k]
                if temp ==x:
                    return True
                if temp<x:
                    j+=1
                else:
                    k-=1
        return False
