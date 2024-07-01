'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''



Approach 1:

def convert(head):
    temp = head
    result = []
    while temp:
        result.append(temp.data)
        temp =temp.next
    i = 0
    T = Tree(result[i])
    check = T
    length = len(result)
    def solve(T,i):
        if (2*i+1)<length:
            T.left = Tree(result[2*i+1])
            solve(T.left,2*i+1)
        if (2*i+2)<length:
            T.right= Tree(result[2*i+2])
            solve(T.right,2*i+2)
    solve(T,i)
    return check


Approach 2:


from collections import deque
#Function to make binary tree from linked list.
def convert(head):
    q = deque()
   
    if not head:
        return
    T = Tree(head.data)
    q.append(T)
    head = head.next
    while head:
        temp = q.popleft()
        if head:
            temp.left = Tree(head.data)
            q.append(temp.left)
            head = head.next
        if head:
            temp.right = Tree(head.data)
            q.append(temp.right)
            head = head.next
    return T
