'''
https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1
'''
class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,del_node):
        del_node.data = del_node.next.data
        del_node.next=del_node.next.next
