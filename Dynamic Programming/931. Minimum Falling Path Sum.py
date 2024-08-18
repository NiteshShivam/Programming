'''
https://leetcode.com/problems/minimum-falling-path-sum/description/
https://www.youtube.com/watch?v=EQC0ckOyEGs
'''
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for i in range(1,len(arr)):
            for j in range(len(arr[0])):
                if j==0:
                    arr[i][j] += min(arr[i-1][j],arr[i-1][j+1])
                elif j == len(arr[0])-1:
                    arr[i][j]+= min(arr[i-1][j],arr[i-1][j-1])
                else:
                    arr[i][j] += min(arr[i-1][j-1],arr[i-1][j],arr[i-1][j+1])
        
        return min(arr[-1])


==========================
class Solution:
   
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[float('inf')]*m for i in range(n)]
        def solve(row,col):
            if row<0 or row>=n or col<0 or col>=m:
                return float('inf')
            if row==n-1:
                return matrix[row][col]
            
            if dp[row][col]!=float('inf'):
                return dp[row][col]
            left = solve(row+1,col-1)
            right =solve(row+1,col+1)
            middle = solve(row+1,col)
            dp[row][col]= matrix[row][col] + min(left,right,middle)
            return dp[row][col]
        result = float('inf')
        for i in range(m):
            result = min(result,solve(0,i))
        return result
