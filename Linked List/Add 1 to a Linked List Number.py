'''
geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
'''
class Solution:
    def reverse(self,head):
        prev = None
        curr = None
        temp =head
        while temp:
            curr  = temp.next
            temp.next = prev
            prev = temp
            temp = curr
        return prev
            
    def addOne(self,head):
        head = self.reverse(head)
        temp = head
        current = 1
        prev = None
        while temp:
            
            current = current+temp.data
            temp.data = current%10
            current = current//10
            prev =temp
            temp=temp.next
        if current>0:
            prev.next = Node(current)
            
        head = self.reverse(head)
        return head
        
