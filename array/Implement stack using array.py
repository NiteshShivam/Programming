'''
https://www.geeksforgeeks.org/problems/implement-stack-using-array/1
'''
class MyStack:
    
    def __init__(self):
        self.arr=[0]*1000
        self.size = 0
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.arr[self.size]=data
        self.size+=1
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.size<=0:
            return -1
        self.size-=1
        return self.arr[self.size]
        
