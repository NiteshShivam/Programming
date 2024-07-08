'''
Given an array arr of non-negative numbers. The task is to find the first equilibrium point in an array. 
The equilibrium point in an array is an index (or position) such that the
sum of all elements before that index is the same as the sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
'''
class Solution:
    # Complete this function
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr):
        allSum = sum(arr)
        length = len(arr)
        prev = 0
        for i in range(length):
            right = allSum-arr[i]-prev
            if right==prev:
                return i+1
            prev +=arr[i]
        return -1
