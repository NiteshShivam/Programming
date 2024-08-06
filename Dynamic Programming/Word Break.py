'''
https://youtu.be/oBUpyPZ08zU
https://www.geeksforgeeks.org/problems/word-break1352/1
'''
class Solution:
    def solve(self,s,index):
        if index>=self.length:
            return True
        if s[index:] in self.dictionary:
            return True
        if self.dp[index]!=-1:
            return self.dp[index]
        for i in range(1,self.length+1):
            if s[index:i+index] in self.dictionary and self.solve(s,i+index):
                    self.dp[index]=True
                    return True
                # return False
        self.dp[index]=False
        return False
    def wordBreak(self, n, s, dictionary):
        index=0
        self.dictionary = set(dictionary)
        self.length  = len(s)
        self.dp = [-1]*(self.length+1)
        
        return self.solve(s,index)
