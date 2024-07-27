'''

https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1
https://www.youtube.com/watch?v=99S-xuAbwoc

https://www.youtube.com/watch?v=jEDPdAwnxV0
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






=========================================


class Solution:
    def countMin(self, str):
        length = len(str)
        dp = [[0]*length for i in range(length)]
        
        for L in range(2,length+1):
            for i in range(length-L+1):
                j = i+L-1
                if str[i] ==str[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j],dp[i][j-1])
            
        return dp[0][length-1]
