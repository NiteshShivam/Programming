'''
https://www.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1
https://youtu.be/S49zeUjeUL0
'''
class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def solve(self,egg,floor):
        if egg==1:
            return floor
        if floor==0 or floor==1:
            return floor
        ans = float('inf')
        if self.dp[egg][floor]!=-1:
            return self.dp[egg][floor]
        for k in range(1,floor+1):
            temp = 1 + max(self.solve(egg-1,k-1),self.solve(egg,floor-k))
            ans = min(ans,temp)
        self.dp[egg][floor] = ans
        return ans
    def eggDrop(self,n, k):
        self.dp = [[-1]*(k+1) for i in range(n+1)]
        return self.solve(n,k)
