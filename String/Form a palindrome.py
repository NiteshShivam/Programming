'''

https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1
https://www.youtube.com/watch?v=99S-xuAbwoc
'''
class Solution:
    def solve(self,i,j,s):
        if i>=j:
            return 0
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
        if s[i]==s[j]:
            self.dp[i][j]= self.solve(i+1,j-1,s)
            return self.dp[i][j]
        else:
            self.dp[i][j] = 1 + min(self.solve(i+1,j,s),self.solve(i,j-1,s))
            return self.dp[i][j]
    def countMin(self, str):
        
        j = len(str)
        self.dp =[[-1]*j for _ in range(j)]
        j = j-1
        return self.solve(0,j,str)
