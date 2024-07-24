'''

https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
'''
class Solution:
    def __init__(self):
        self.dp = None
    def solve(self,i,N,arr,sum):
        if sum==0:
            return True
        if sum<0:
            return False
        if i>=N:
            return False
        if self.dp[sum][i]!=-1:
            return self.dp[sum][i]
        self.dp[sum][i]= self.solve(i+1,N,arr,sum-arr[i]) or self.solve(i+1,N,arr,sum)
        return self.dp[sum][i]
    def isSubsetSum (self, N, arr, sum):
        self.dp = [[-1]*(N+1) for _ in range(sum+1)]
        i=0
        return self.solve(i,N,arr,sum)
