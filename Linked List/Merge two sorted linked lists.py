'''
https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1
'''

'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to merge two sorted linked list.
    def sortedMerge(self,head1, head2):
        
        T = Node(0)
        F = T
        while  head1 and head2:
            if head1.data<=head2.data:
                T.next=head1
                T = T.next
                head1=head1.next
            else:
                T.next=head2
                T =T.next
                head2 = head2.next
        if head1:
            T.next =head1
        if head2:
            T.next = head2
        return F.next
