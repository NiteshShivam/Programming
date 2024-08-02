'''
https://www.geeksforgeeks.org/queue-in-python/
https://www.geeksforgeeks.org/problems/stack-using-two-queues/1
'''
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue   
   

#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    if not queue_2.empty():
        queue_2.put(x)
    else :
        queue_1.put(x)
   

#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    if queue_1.empty() and queue_2.empty():
        return -1
    
    if not queue_1.empty():
        while queue_1.qsize()!=1:
            queue_2.put(queue_1.get())
        return queue_1.get()
    else:
        while queue_2.qsize()!=1:
            queue_1.put(queue_2.get())
        return queue_2.get()
