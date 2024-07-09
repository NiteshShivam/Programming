'''
Given an array, arr of integers, and another number target,
find three integers in the array such that their sum is closest to the target.
Return the sum of the three integers.

Note: If there are multiple solutions, return the maximum one.

https://www.geeksforgeeks.org/problems/three-sum-closest/1
https://youtu.be/hGLjwiPRh0U
'''
class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        length = len(arr)
        arr.sort()
        finalSum = -1e9
        absoluteRe =1e9
        for k in range(length-2):
            i = k+1
            j = length-1
            while i<j:
                cSum = arr[k]+arr[i]+arr[j]
                difference = abs(target-cSum)
                if difference<absoluteRe:
                    absoluteRe = difference
                    finalSum = cSum
                elif difference==absoluteRe:
                    finalSum = max(finalSum,cSum)
                #if finalSum==target:
                #    return target
                if cSum<target:
                    i+=1
                else:
                    j-=1
        return finalSum
