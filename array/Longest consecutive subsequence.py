 '''
 Given an array of non-negative integers. Find the length of the longest sub-sequence
 such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.

 https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
 '''
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        s = set()
        maxE = arr[0]
        for each in arr:
            s.add(each)
            maxE = max(maxE,each)
        result = 0
        current = 0
        for i in range(maxE+1):
            if i not in s:
                result = max(result,current)
                current =0
            else:
                current+=1
        result = max(current,result)
        return result
