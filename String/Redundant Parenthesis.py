'''

https://www.geeksforgeeks.org/problems/redundant-parenthesis--170647/1
'''
from collections import deque
class Solution:
    def removeBrackets (self, a):
        n = len(a)
        s = deque()
        op = deque()
        del_flag = [0]*n
        for i in range(n):
            c = a[i]
            if c.isalpha():
                continue
            if c==")":
                addSub = False
                mulDiv = False
                if a[s[-1]]=="(":
                    del_flag[i]=1
                    del_flag[s[-1]]=1
                    s.pop()
                else:
                    while a[s[-1]]!='(':
                        d = a[s[-1]]
                        s.pop()
                        op.pop()
                        
                        if d=='*' or d=='/':
                            mulDiv = True 
                        else:
                            addSub =True
                    ind =s.pop()
                    if len(op)==0:
                        del_flag[i]=1
                        del_flag[ind]=1
                        continue
                    d = a[op[-1]]
                    if d=="+" or ((d=="*" or d=='-') and  not addSub) :
                        del_flag[i]=1
                        del_flag[ind]=1
                    
                    
                        
            elif c=="(":
                s.append(i)
            else:
                s.append(i)
                op.append(i)
        ans = "".join(a[k] for k in range(n) if not del_flag[k])
        return ans
