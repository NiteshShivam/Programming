'''
Given an array a[ ] of n integers, find the Length of the Longest Strictly Increasing Subsequence.

A sequence of numbers is called "strictly increasing" when each
term in the sequence is smaller than the term that comes after it.


https://www.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
https://www.youtube.com/watch?v=DG50PJIx2SM
https://www.youtube.com/watch?v=h9rm4N8XbL0

last apporach will pass : O(n*logn)
https://www.youtube.com/watch?v=on2hvxBXJH4
'''
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, arr):
        # code here
        dp = [1]*n
        for i in range(1,n):
           for j in range(i-1,-1,-1):
               if arr[i]>arr[j]:
                   dp[i]= max(dp[j]+1,dp[i])
                   
        for i in range(n):
            dp[0] = max(dp[0],dp[i])
        return dp[0]
========================================================================================================================================================================
Approach 2:

class Solution:

    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, arr):
        # code here
        dp = [[-1]*(n+1) for i in range(n+1)]
        def solve(i,p):
            if i>=n:
                return 0
            take,skip=0,0
            if dp[i][p]!=-1:
                return dp[i][p]
            if p==-1 or arr[p]<arr[i]:
                take = 1+solve(i+1,i)
            skip = solve(i+1,p)
            if p!=-1:
                dp[i][p] = max(take,skip)
            return max(take,skip)
            
        return solve(0,-1)

========================================================================================================================================================================
class Solution:

    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, arr):
        space = [arr[0]]
        for i in range(1,n):
            if space[-1]<arr[i]:
                space.append(arr[i])
            else:
                
                left = 0
                rigth = len(space)-1
                while left<rigth:
                    mid = left+(rigth-left)//2
                    if space[mid]<arr[i]:
                        left  =mid+1
                    else:
                        
                        rigth = mid
                space[left]=arr[i]
        return len(space)
