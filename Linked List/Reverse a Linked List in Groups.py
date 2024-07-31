'''
https://www.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
'''

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reveseBetween(self,head,h2):
        prev = None
        temp = head
        while temp!=h2:
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode
        return prev,head
            
    def reverse(self,head, k):
        count = 0
        temp = head
        tempHead = head
        head = None
        prevTail = None
        while temp:
            count+=1
            if count==k:
                count=0
                newTemp=temp.next
                currenthead,currenttail = self.reveseBetween(tempHead,temp.next)
                if not head:
                    head = currenthead
                else:
                    prevTail.next = currenthead
                prevTail = currenttail
                temp = newTemp
                tempHead=temp
                
            else:
                temp = temp.next
        if count!=0:
            currenthead,currenttail = self.reveseBetween(tempHead,temp)
            if not head:
                    head = currenthead
                    prevTail = currenttail
            else:
                prevTail.next = currenthead
                prevTail = currenttail
        return head
        
