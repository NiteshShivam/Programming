'''
Given a sorted array arr containing n elements with possibly some duplicate, 
the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.



https://youtu.be/jpuDyt-ruFc
https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
'''

class Solution:
    
    
    def find(self, arr, n, x):
        def findLeftMost():
            i = 0
            j = n-1
            left_most= -1
            while i<=j:
                mid = i+(j-i)//2
                if arr[mid]==x:
                    left_most=mid
                    j = mid-1
                elif arr[mid]>x:
                    j = mid-1
                else:
                    i=mid+1
            return left_most
        def findRightMost():
            i = 0
            j = n-1
            right_most = -1
            while i<=j:
                mid = i+(j-i)//2
                if arr[mid]==x:
                    right_most=mid
                    i = mid+1
                elif arr[mid]>x:
                    j = mid-1
                else:
                    i = mid+1
            return right_most
        left_most = findLeftMost()
        right_most = findRightMost()
       
        return [left_most,right_most]

