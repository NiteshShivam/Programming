'''
Note : it's hard question,hard to understand,let it go.
https://leetcode.com/problems/strange-printer/description/
https://youtu.be/pV3arpA0TzY
'''
class Solution:
    def solve(self,l,r,s):
        if l==r:
            return 1
        if l>r:
            return 0
        if self.dp[l][r]!=-1:
            return self.dp[l][r]
        i = l+1

        while i<=r and s[i]==s[l]:
            i+=1
        if(i==r+1):
            return 1
        basic = 1+self.solve(i,r,s)
        lalch = float('inf')
        for j in range(i,r+1):
            if(s[j]==s[l]):
                ans = self.solve(i,j-1,s)+self.solve(j,r,s)
                lalch = min(lalch,ans)
        self.dp[l][r] = min(basic,lalch)
        return self.dp[l][r]
    def strangePrinter(self, s: str) -> int:
        self.n =len(s)
        self.dp = [[-1]*(self.n+1) for _ in range(self.n+1)]
        return self.solve(0,self.n-1,s)
