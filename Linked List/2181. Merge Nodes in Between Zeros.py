You are given the head of a linked list, which contains a series of integers separated by 0's. 
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them
into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Approach :

Return the head of the modified linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        temp2 = head.next
        currentSum = 0
        while temp2:
            if temp2.val==0:
                temp1 = temp1.next
                temp1.val = currentSum
                currentSum=0
                
            currentSum = currentSum+temp2.val
            temp2 = temp2.next
        temp1.next=None
        return head.next



Approach 2: recursion:

class Solution:
    def solve(self,head,temp,currentSum):
        if not head:
            #temp = temp.next
            #temp.val=currentSum
            temp.next=None
            return
        if head.val==0:
            temp = temp.next
            temp.val = currentSum
            currentSum = 0
        currentSum = currentSum+head.val
        head=head.next
        
        self.solve(head,temp,currentSum)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        currentSum=0
        self.solve(head.next,temp,currentSum)
        return head.next


#Approach 3 : recursion:

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head=head.next
        temp=head
        if not temp:
            return head
        current=0
        while temp and temp.val!=0:
            current+=temp.val
            temp=temp.next
        head.val=current
        head.next=self.mergeNodes(temp)
        return head
