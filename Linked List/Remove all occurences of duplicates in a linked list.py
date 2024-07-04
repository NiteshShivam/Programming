"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""

class Solution:
    def removeAllDuplicates(self, head):
        #code here
        temp = head
        dummy = Node(0)
        prev = dummy
        while temp:
            currVal=temp.data
            if temp.next and temp.next.data==currVal:
                while temp and currVal==temp.data:
                    temp = temp.next
                prev.next = temp
            else:
                prev.next=temp
                prev = prev.next
                temp=temp.next
            
        return dummy.next
