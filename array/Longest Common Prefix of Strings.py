'''
Given an array of strings, 
Return the longest common prefix among all strings present in the array.
If there's no prefix common in all the strings, return "-1".



https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1
'''
class Solution:
    def longestCommonPrefix(self, n, arr):
        minString = arr[0]
        for i in range(1,n):
            if len(arr[i])<len(minString):
                minString = arr[i]
        length = len(minString)
        result = ""
        for i in range(length):
            for j in range(n):
                if minString[:i+1]!=arr[j][:i+1]:
                    if len(result)>0:
                        return result
                    return -1
            result = minString[:i+1]
        return result
