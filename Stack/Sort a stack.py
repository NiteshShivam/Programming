'''
https://www.geeksforgeeks.org/problems/sort-a-stack/1
'''
class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        def insertStack(s,temp):
            if len(s)==0 or s[-1]<temp:
                s.append(temp)
                return
            else:
                temp1 = s.pop()
                insertStack(s,temp)
                s.append(temp1)
        def sortStack(s):
            if len(s)!=0:
                temp = s.pop()
                sortStack(s)
                insertStack(s,temp)
        sortStack(s)
