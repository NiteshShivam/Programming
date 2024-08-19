'''
https://leetcode.com/problems/2-keys-keyboard/description/
https://youtu.be/zELBK8_vB7Y
'''
class Solution:
    def solve(self,n,count,clip):
        if count==n:
            return 0
        if count>n:
            return float('inf')
        if self.dp[count][clip]!=-1:
            return self.dp[count][clip]
        
        paste = 1 + self.solve(n,count+clip,clip)
        copy_paste = 2 + self.solve(n,count+count,count)
        self.dp[count][clip] =  min(copy_paste,paste)
        return self.dp[count][clip]
    def minSteps(self, n: int) -> int:
        self.dp = [[-1]*(n+1) for _ in range(n+1)]
        result = 1
        current = 1
        if n==1:
            return 0
        return  1+self.solve(n,result,current)





===============================
class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        if n==2:
            return 2
        dp = [0]*(n+1)
        dp[1]=0
        dp[2]=2
        for i in range(3,n+1):
            factor = i//2
            while factor>=1:
                if i%factor==0:
                    copy = 1
                    result = i//factor-1
                    dp[i] = dp[factor]+copy+result
                    break
                else:
                    factor-=1
        return dp[n]








===========================
class Solution:
    def solve(self,n,count,clip):
        if count==n:
            return 0
        if count>n:
            return float('inf')
        if (count,clip) in self.dp:
            return self.dp[(count,clip)]
        
        paste = 1 + self.solve(n,count+clip,clip)
        copy_paste = 2 + self.solve(n,count+count,count)
        self.dp[(count,clip)] =  min(copy_paste,paste)
        return self.dp[(count,clip)]
    def minSteps(self, n: int) -> int:
        self.dp = {}
        result = 1
        current = 1
        if n==1:
            return 0
        return  1+self.solve(n,result,current)
