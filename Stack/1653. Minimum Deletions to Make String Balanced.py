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
