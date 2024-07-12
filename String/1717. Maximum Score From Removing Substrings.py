'''
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.



https://leetcode.com/problems/maximum-score-from-removing-substrings/description/
'''
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack =deque()
        length = len(s)
        def calculate(s,substring,points):
            stack = deque()
            profit = 0
            for c in s:
                if stack and stack[-1]+c==substring:
                    stack.pop()
                    profit +=points
                else:
                    stack.append(c)
            newS = ""
            for c in stack:
                newS+=c
            return profit,newS
        def finalC(s,sub1,sub2,x,y):
            stack = deque()
            profit = 0
            for c in s:
                if stack and (stack[-1]+c==sub1 or stack[-1]+c==sub2):
                    if stack[-1]+c==sub1:
                        profit +=x
                    else:
                        profit +=y
                    stack.pop()
                else:
                    stack.append(c)
            return profit
            
        result = 0
        newS = ""
        if x>y:
            result,newS = calculate(s,"ab",x)
        else:
            result,newS = calculate(s,'ba',y)
        result += finalC(newS,"ab","ba",x,y)
        return result
        
