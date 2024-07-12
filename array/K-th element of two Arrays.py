'''
Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. 
The task is to find the element that would be at the kth position of the final sorted array.

 
https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
'''
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i = 0
        j = 0
        k-=1
        while k>0:
            if i<n and (j>=m or arr1[i]<=arr2[j]):
                i+=1
            elif j<m and( i>=n or arr1[i]>arr2[j]):
                j+=1
            k-=1
        if i<n and (j>=m or arr1[i]<arr2[j]):
            return arr1[i]
        return arr2[j]
