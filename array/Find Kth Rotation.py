'''
https://www.geeksforgeeks.org/problems/rotation4723/1
'''
class Solution:
    def findKRotation(self, arr):
        length = len(arr)
        result = 0
        count = 0
        for i in range(length-1):
            if arr[i]>arr[i+1]:
                count+=1
                result = count
                break
            count+=1
        return result
