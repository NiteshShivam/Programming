'''
Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and 
modify the original array such that all the distinct elements come at the beginning of the original array.



https://www.youtube.com/watch?v=06ALbFrgIoQ

https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
'''
class Solution:
    def remove_duplicate(self, arr):
        length = len(arr)
        i = 0
        j = 0
        while  j<length:
            if arr[i]!=arr[j]:
                i+=1
                arr[i]=arr[j]
            j+=1
        return i+1
