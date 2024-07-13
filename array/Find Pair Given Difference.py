'''

Given an array arr[] of size n and an integer x, 
return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.


https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1
'''
from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        arr.sort()
        i = 0
        j = 1
        while i <n and j<n:
            diff = arr[j]-arr[i]
            if diff==x and i!=j:
                return 1
            if diff>x:
                i+=1
            else:
                j+=1
        return -1
