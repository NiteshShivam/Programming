'''
Given a singly linked list's head. The task is to left-shift the linked list by k nodes,
where k is a given positive integer smaller than or equal to length of the linked list.


https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1
'''
class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        temp = head
        while temp.next:
            temp = temp.next
        while k>0:
            temp.next = head
            head = head.next
            temp = temp.next
            temp.next = None
            k-=1
        return head
