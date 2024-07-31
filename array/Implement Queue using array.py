'''
https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
'''
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear=0
    
    def push(self, x):
        self.arr.append(x)
        self.rear+=1
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if self.front==self.rear:
            return -1
        t =  self.arr[self.front]
        self.front+=1
        return t
