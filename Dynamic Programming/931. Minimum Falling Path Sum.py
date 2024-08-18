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
