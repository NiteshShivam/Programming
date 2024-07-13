'''
Given an array having both positive and negative integers. 
The task is to compute the length of the largest subarray with sum 0.


https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
'''
class Solution:
    def maxLen(self, n, arr):
        currentSum = 0
        hashMap ={}
        hashMap[0]=-1
        result = 0
        for i in range(n):
            temp = arr[i]
            currentSum=temp+currentSum
            if currentSum in hashMap:
                result = max(result,i-hashMap[currentSum])
            else:
                hashMap[currentSum]=i
        return result
