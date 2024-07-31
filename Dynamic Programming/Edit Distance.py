'''

https://youtu.be/oqfqPEqrKo8
https://www.geeksforgeeks.org/problems/edit-distance3702/1
'''
class Solution:
    def solve(self,i,j):
        if i==self.m or j==self.n:
            if j==self.n:
                return self.m-i
            return self.n-j
        else:
            if self.dp[i][j]!=-1:
                return self.dp[i][j]
            if self.s[i]==self.t[j]:
                return self.solve(i+1,j+1)
            # insert
            insert =1+self.solve(i,j+1)
            # delete
            delete = 1+self.solve(i+1,j)
            #replace
            replace =1+ self.solve(i+1,j+1)
            self.dp[i][j] = min(insert,delete,replace)
            return min(insert,delete,replace)
        
	def editDistance(self, s, t):
		
		self.s =s 
		self.t =t
		self.m = len(s)
		self.n = len(t)
		self.dp = [[-1]*(self.n+1) for _ in range(self.m+1)]
		return self.solve(0,0)

===========================================

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
		
