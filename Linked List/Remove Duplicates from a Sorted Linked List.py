'''Given a singly linked list consisting of N nodes. 
The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
Note: Try not to use extra space. The nodes are arranged in a sorted way.
'''

#Appraoch : 
def removeDuplicates(head):
    #code here
    temp = head
    while temp and temp.next:
        if temp.data==temp.next.data:
            temp.next=temp.next.next
        else:
            temp = temp.next
    return head
