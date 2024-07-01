class Solution:
    
    def reverseList(self, head):
        prev = None
        curr = None
        while head:
            curr = head.next
            head.next=prev
            prev =head
            head=curr
        return prev

