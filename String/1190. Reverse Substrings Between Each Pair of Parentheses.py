'''

https://www.youtube.com/watch?v=dUQRS4luBvA&t=959s
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
'''
from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        length = len(s)
        space =[]
        for i in range(length):
            space.append(s[i])
        for i in range(length):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                t = stack.pop()
                space[t:i] = reversed(space[t:i])
        result = ""
        for i in range(length):
            if space[i]!="(" and space[i]!=")":
                result+=space[i]
        return result
==================================================================

from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque()
        length = len(s)
        send  =""
        for i in range(length):
            if s[i]=="(":
                stack.append(len(send))
            elif s[i]==")":
                t = stack.pop()
                send = send[:t]+send[t:][::-1]   
            else:
                send+=s[i]
        return send
