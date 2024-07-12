'''
Given a sorted array arr[] of size n without duplicates, and given a value x. 
Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x. 
Find the index of k(0-based indexing).




https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

'''
class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,N,X):
        left =0
        right =N-1
        ans =-1
        while left<=right:
            mid = left+(right-left)//2
            if arr[mid]==X:
                return mid
            elif arr[mid]>X:
                right = mid-1
            else:
                ans = mid
                left = mid+1
       
        return ans
        
