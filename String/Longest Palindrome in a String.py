'''
https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1
'''
class Solution:
    def longestPalin(self, S):
        # code here
        length = len(S)
        result = 0
        start = 0
        end = 0
        for i in range(length):
            l = i
            r = i
            while l>=0 and r<length:
                if S[l]!=S[r]:
                    break
                l-=1
                r+=1
            le = r-l-1
            if result<le:
                result = le
                start = l+1
                end = r-1
        
        for i in range(length):
            l = i
            r = i+1
            while l>=0 and r<length:
                if S[l]!=S[r]:
                    break
                l-=1
                r+=1
            le = r-l-1
            if result<le:
                result = le
                start = l+1
                end = r-1
        return S[start:start+result]
        


==========================
class Solution:
    def longestPalin(self, S):
        length = len(S)
        dp = [[False]*length for i in range(length)]
        for i in range(length):
            dp[i][i]=True
        def solve(i,j):
            if i>=j:
                return True
            if dp[i][j]:
                return True
            if S[i]==S[j]:
                dp[i][j]=solve(i+1,j-1)
                return dp[i][j] 
            dp[i][j]=False
            return dp[i][j]
        # code here
        
        
        result = 0
        sp=0 
        for i in range(length):
            for j in range(i,length):
                if solve(i,j):
                    if result<(j-i+1):
                        result = j-i+1
                        sp = i
        return S[sp:sp+result]

