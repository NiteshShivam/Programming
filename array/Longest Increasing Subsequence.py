
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
