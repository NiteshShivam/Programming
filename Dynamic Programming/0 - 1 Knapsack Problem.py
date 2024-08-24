'''
https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
'''

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dynamic = [[0]*(W+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    dynamic[i][j] = max(dynamic[i-1][j],val[i-1]+dynamic[i-1][j-wt[i-1]])
                else:
                    dynamic[i][j]=dynamic[i-1][j]
        return dynamic[n][W]
        





========================
class Solution:
    
   
    def knapSack(self,W, wt, val):
        length = len(val)
        def solve(i,W):
            if i>=length:
                return 0
            
            left = 0
            if W>=wt[i]:
                left = val[i]+solve(i+1,W-wt[i])
            right = solve(i+1,W)
            return max(left,right)
        return solve(0,W)
    
