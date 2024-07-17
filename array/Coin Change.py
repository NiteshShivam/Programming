'''
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum,
find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.



https://www.youtube.com/watch?v=HhSZQkdJZok
https://www.geeksforgeeks.org/problems/coin-change2448/1
'''
class Solution:
    
    def count(self, arr, N, Sum):
        dp =[[-1]*(N+1) for _ in range(Sum+1)]
        def solve(i,amount):
            if i>=N or amount<0:
                return 0
            if amount==0:
                return 1
            if dp[amount][i]!=-1:
                return dp[amount][i]
            
            l = solve(i,amount-arr[i])
            r = solve(i+1,amount)
            dp[amount][i] = l+r
            return l+r
        return solve(0,Sum)
