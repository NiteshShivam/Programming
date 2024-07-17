'''

Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need to return true/false depending upon 
whether there is a subarray present with 0-sum or not. Printing will be taken care by the driver code.

https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
'''
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        solve = {}
        solve[0]=-1
        current = 0
        for i in range(n):
            current = current+arr[i]
            if current in solve:
                return True
            solve[current]=i
        return False
