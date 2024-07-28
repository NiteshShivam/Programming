'''
https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
'''
class Solution:
    
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if S2[i-1]==S1[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
        result = 0
        for i in range(m+1):
            for j in range(n+1):
                result = max(result,dp[i][j])
        return result
