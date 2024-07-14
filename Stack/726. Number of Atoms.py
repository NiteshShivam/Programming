'''

https://www.youtube.com/watch?v=XnVWIT47H0Y
https://leetcode.com/problems/number-of-atoms/description/
'''
from collections import deque,OrderedDict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        hashM = {}
        stack = deque()
        length = len(formula)
        n=length
        i = 0
        stack.append({})
        while i<length:
            if formula[i]=="(":
                stack.append({})
                i+=1
            elif formula[i]==")":
                current = stack.pop()
                i+=1
                multiply = ""
                while i<n and formula[i].isdigit():
                    multiply+=formula[i]
                    i+=1
                if len(multiply)>0:
                    multiply = int(multiply)
                    for key,value in current.items():
                        current[key]*=multiply
                for key,value in current.items():
                    if key in stack[-1]:
                        stack[-1][key]+=value
                    else:
                        stack[-1][key]=value
            else:
                currentS = formula[i]
                i+=1
                while i<n and formula[i].isalpha() and formula[i].islower():
                    currentS +=formula[i]
                    i+=1
                currentCount =""
                while i<n and formula[i].isdigit():
                    currentCount+=formula[i]
                    i+=1
                if len(currentCount)==0:
                    currentCount=1
                currentCount = int(currentCount)
                if currentS in stack[-1]:
                    stack[-1][currentS]+=currentCount
                else:
                    stack[-1][currentS]=currentCount
                #stack[-1][currentS] = stack[-1].get(currentS,0)+=currentCount
        orderMap = sorted(stack[-1].keys())
        print(orderMap)
        result = ""
        for key in orderMap:
            result +=key
            value = stack[-1][key]
            if value>1:
                result +=str(value)
        return result
