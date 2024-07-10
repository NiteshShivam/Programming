'''
Given an array arr[] of size n of non-negative integers. Each array element represents
the maximum length of the jumps that can be made forward from that element. 
This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. 
If an element is 0, then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.


https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
https://www.youtube.com/watch?v=vBdo7wtwlXs
'''
#User function Template for python3
import sys
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n==0 or n==1:
	        return 0
	    if arr[0]==0:
	        return -1
	    
	    dp = [sys.maxsize]*n
	    dp[0]=0
	    for i in range(1,n):
	        for j in range(i):
	            if arr[j]+j>=i:
	                if dp[i]>dp[j]+1:
	                    dp[i]=dp[j]+1
	  
	   
	    if dp[n-1]==sys.maxsize:
	        return -1
	    return dp[n-1]
============================================================================================

Approach 2:
#User function Template for python3
import sys
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if n==0 or n==1:
	        return 0
	    if arr[0]==0:
	        return -1
	    ladder = arr[0]
	    stair = arr[0]
	    level = 1
	    jumps = 1
	    while level<n:
	        if level==n-1:
	            return jumps
	        if stair:
	            if level+arr[level]>ladder:
	                ladder= level+arr[level]
	            stair-=1
	        if stair==0:
	            if level>=ladder:
	                return -1
	            jumps+=1
	            stair = ladder-level
	        level+=1
	    return -1
