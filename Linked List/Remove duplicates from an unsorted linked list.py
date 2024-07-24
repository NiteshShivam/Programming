'''
https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1
'''
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        temp = head
        space = set()
        prev = None
        while temp:
            if temp.data not in space:
                prev = temp
                space.add(temp.data)
                temp = temp.next
            else:
                while temp and  temp.data in space:
                    temp = temp.next
                prev.next =temp
            
        
        return head
        

