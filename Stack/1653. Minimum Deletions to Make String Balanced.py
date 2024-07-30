'''
https://www.youtube.com/watch?v=gorAMHTwDfU
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/
'''
from collections import deque
class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0
        stack =deque()
        for ch in s:
            if ch=='a':
                if stack and stack[-1]=='b':
                    stack.pop()
                    result+=1
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return result


===============================

class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0
        a = []
        length = len(s)
        b = [0]*length
        bcount = 0
        acount = 0
        i = -1
        for ch in s:
            a.append(acount)
            if ch=='b':
                acount+=1
            b[i]=bcount
            if s[i]=='a':
                bcount+=1
            i-=1
        result = 2*length
        for i in range(length):
            result = min(result,a[i]+b[i])
        return result
        return result
