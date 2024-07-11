'''
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
