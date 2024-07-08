'''
Given a sorted array containing only 0s and 1s, find the transition point, i.e.,
the first index where 1 was observed, and before that, only 0 was observed.

https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1

'''

class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        left = 0
        right = n-1
        while left<right:
            mid = left+(right-left)//2
            if arr[mid]==1:
                right=mid
            elif arr[mid]==0:
                left =mid+1
            else:
                right=mid-1
        if arr[left]==0:
            return -1
        return right
        # return left #both okay
