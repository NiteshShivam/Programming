'''
https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1
https://youtu.be/jnj87BSi9Is
'''

class Solution:
    def __init__(self):
        self.rightminHeap = []
        self.leftmaxHeap = []
        self.count = 0
    def balanceHeaps(self):
        if len(self.leftmaxHeap)>len(self.rightminHeap)+1:
            x = heapq.heappop(self.leftmaxHeap)
            heapq.heappush(self.rightminHeap,-x)
        elif len(self.leftmaxHeap)<len(self.rightminHeap):
            x = heapq.heappop(self.rightminHeap)
            heapq.heappush(self.leftmaxHeap,-x)
            
        
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if self.count%2==0:
            return (-self.leftmaxHeap[0] + self.rightminHeap[0])/2
        else:
            return -(self.leftmaxHeap[0])
        
        
    def insertHeaps(self,x):
        if len(self.leftmaxHeap)==0:
            heapq.heappush(self.leftmaxHeap,-x)
        else:
            if -(self.leftmaxHeap[0])<x:
                heapq.heappush(self.rightminHeap,x)
            else:
                heapq.heappush(self.leftmaxHeap,-x)
        
        self.count+=1
        self.balanceHeaps()
