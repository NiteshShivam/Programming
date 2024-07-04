#You are given N operations and your task is to Implement a Stack in which you can get a minimum element in O(1) time.

#Approach : 
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if not self.s:
            self.minEle=x
            self.s.append(x)
        else:
            if self.minEle<x:
                self.s.append(x)
            else:
                t = 2*x-self.minEle
                self.s.append(t)
                self.minEle =x
       
    def pop(self):
        if not self.s:
            return -1
        #CODE HERE
        if self.s[-1]>self.minEle:
            return self.s.pop()
        else:
            t = self.minEle
            self.minEle = self.minEle*2-self.s[-1]
            self.s.pop()
            return t
        #return self.s.pop()

    def getMin(self):
        if not  self.s:
            return -1
        #CODE HERE
        return self.minEle

