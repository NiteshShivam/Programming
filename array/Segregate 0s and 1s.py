'''
Given an array arr consisting of only 0's and 1's in random order.
Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
'''
class Solution:
    def segregate0and1(self, arr):
        i = 0
        j = len(arr)-1
        while i<j:
            if arr[i]==0:
                i+=1
            if arr[j]==1:
                j-=1
            if i<j and arr[i]==1 and arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
