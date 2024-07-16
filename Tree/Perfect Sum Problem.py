'''
https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
'''
class Solution:
    
	def perfectSum(self, arr, n, k):
	    mod = 10**9+7
	    dp = [[-1] * (k + 1) for _ in range(n + 1)]
		def solve(i,current):
            if i>=n:
                if current==k:
                    return 1
                return 0
            
            if current>k:
                return 0
            if dp[i][current]!=-1:
                return dp[i][current]
            left = solve(i+1,current+arr[i])
            right = solve(i+1,current)
            dp[i][current]=(left+right)%mod
            return dp[i][current]
        return solve(0,0)
