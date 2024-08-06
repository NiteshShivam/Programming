'''
https://www.geeksforgeeks.org/problems/word-break-part-23249/1
https://youtu.be/TmkRMtbXVPw
'''
class Solution:
    def solve(self,index,currentS,s):
        if index>=self.length:
            self.result.append(currentS)
            return
        for j in range(index,len(s)):
            if s[index:j+1] in self.dict:
                temp  = currentS
                if len(currentS)==0:
                    currentS+=s[index:j+1]
                else:
                    currentS =currentS +" "+s[index:j+1]
                self.solve(1+j,currentS,s)
                currentS = temp
                 
        
    def wordBreak(self, n, dict, s):
        self.result = []
        currentS = ""
        self.dict = set(dict)
        self.length = len(s)
        index =0
        self.solve(index,currentS,s)
        return self.result
