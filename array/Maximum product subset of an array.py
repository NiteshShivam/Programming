'''
Given an array arr. The task is to find and 
return the maximum product possible with the subset of elements present in the array.


Note:
The maximum product can be a single element also.
Since the product can be large, return it modulo 109 + 7.


https://youtu.be/QLUg9v5NJc0
https://www.geeksforgeeks.org/problems/maximum-product-subset-of-an-array/1
'''
class Solution:
    def findMaxProduct(self, arr):
        length = len(arr)
        prod = 1
        max_int = -float('inf')
        mod = 1000000007
        zero=0
        negative= 0
        for i in range(length):
            if arr[i]==0:
                zero+=1
                continue
            if arr[i]<0:
                negative+=1
                max_int = max(max_int,arr[i])
            prod = (prod*arr[i])
            if prod>0:
                prod = prod%mod
            
        if zero==length:
            return 0
        elif negative==1 and zero+negative==length:
            return 0
        elif negative%2==1:
            prod = prod//max_int
        return prod%mod
