'''

https://youtu.be/oqfqPEqrKo8
https://www.geeksforgeeks.org/problems/edit-distance3702/1
'''

class Solution:
	def editDistance(self, s, t):
		lengthS = len(s)
		lengthT = len(t)
		dp = [[0]*(lengthT+1) for i in range(lengthS+1)]
		for i in range(lengthS+1):
		    for j in range(lengthT+1):
		        if i==0:
		            dp[i][j]=j
		        if j==0:
		            dp[i][j]=i
		for i in range(lengthS):
		    for j in range(lengthT):
		        
		        if s[i]==t[j]:
		            dp[i+1][j+1] = dp[i][j]
		        else:
		            dp[i+1][j+1] = 1+min(dp[i][j+1],dp[i+1][j],dp[i][j])
		
		return dp[lengthS][lengthT]    
		
