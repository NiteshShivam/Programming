'''Given two strings str1 & str 2 of length n & m respectively, return the length of their 
longest common subsequence. If there is no common subsequence then, return 0. 

A subsequence is a sequence that can be derived from the given string by deleting 
some or no elements without changing the order of the remaining elements.
For example, "abe" is a subsequence of "abcde".



'''
class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if str2[i]==str1[j]:
                    dp[i+1][j+1]=1 + dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        #print(dp)
        return dp[m][n]

Approach 2: 
class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.dp = None
    def solve(self,i,j,str1,str2):
        if i>=self.n or j>=self.m:
            return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        if str1[i]==str2[j]:
            self.dp[i][j]=1+self.solve(i+1,j+1,str1,str2)
            return self.dp[i][j]
        else:
            self.dp[i][j]= max(self.solve(i+1,j,str1,str2),self.solve(i,j+1,str1,str2))
            return self.dp[i][j]
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        
        # code here
        self.dp = [[-1]*(1001) for _ in range(1001)]
        self.n = n
        self.m = m
        return self.solve(0,0,str1,str2)

