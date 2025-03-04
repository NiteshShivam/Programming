'''

https://www.geeksforgeeks.org/problems/number-of-coins1824/1
'''

class Solution:
    
    def minCoins(self, coins, M, V):
        dp = [float('inf')]*(V+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,V+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[V]==float('inf'):
            return -1
        return dp[V]
        
======================================
import sys
sys.setrecursionlimit(50000)
class Solution:
    def solve(self,v,i,coins):
        if v==0:
            return 0
        if i>=len(coins) or v<0:
            return float('inf')
        if self.dp[v][i]!=-1:
            return self.dp[v][i]
        l  = 1+ self.solve(v-coins[i],i,coins)
        r = self.solve(v,i+1,coins)
        self.dp[v][i]=min(l,r)
        return self.dp[v][i]
    def minCoins(self, coins, M, V):
        self.dp = [[-1 for _ in range(M)] for _ in range(V + 1)]
        a = self.solve(V,0,coins)
        #print(self.dp)
        if a !=float('inf'):
            return a
        return -1
