#User function Template for python3
'''
Given a sorted (in ascending order) and rotated array arr of distinct elements which 
may be rotated at some point and given an element key, the task is to find the index of the given element key in the array arr.
The whole array arr is given as the range to search.

Rotation shifts elements of the array by a certain number of positions, with elements that fall off one end reappearing at the other end.

Note:- 0-based indexing is followed & returns -1 if the key is not present.

https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1
https://youtu.be/U1VsdRgVevY
'''
class Solution:
    def findIndex(self,arr,left,right):
        while left<right :
            mid = left+(right-left)//2
            if arr[mid]>arr[right]:
                left = mid+1
            else:
                right = mid
        return left
    def binary(self,arr,left,right,target):
        while left<=right:
            mid = left+(right-left)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
    def search(self,arr,target):
        if not arr:
            return -1
        length = len(arr)-1
        tempMi = self.findIndex(arr,0,length)
        #print(tempMi)
        if arr[tempMi]==target:
            return tempMi
        left = 0
        first =self.binary(arr,0,tempMi-1,target)
        if first!=-1:
            return first
        second = self.binary(arr,tempMi,length,target)
        if second!=-1:
            return second
        return -1
