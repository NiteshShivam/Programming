'''
Given an array arr[], find the first repeating element. 
The element should occur more than once and the index of its first occurrence should be the smallest.

Note:- The position you return should be according to 1-based indexing.


https://www.geeksforgeeks.org/problems/first-repeating-element4018/1
'''
class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr):
        hashMap = {}
        length = len(arr)
        for i in range(length):
            hashMap[arr[i]] = hashMap.get(arr[i],0)+1
        for i in range(length):
            if hashMap[arr[i]]>1:
                return i+1
        return -1
