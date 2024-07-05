'''
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance]
where minDistance is the minimum distance between any two distinct critical points and
maxDistance is the maximum distance between any two distinct critical points.
If there are fewer than two critical points, return [-1, -1].
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = []
        prev = head
        temp = head.next
        i = 0
        while temp.next:
            if prev.val<temp.val and temp.val>temp.next.val:
                result.append(i)
            elif prev.val>temp.val and temp.val<temp.next.val:
                result.append(i)
            i+=1
            prev = temp
            temp = temp.next
        length = len(result)
        if length<2:
            return [-1,-1]
        maxR = result[-1]-result[0]
        minV = maxR
        for i in range(length-1):
            minV = min(minV,result[i+1]-result[i])
        return [minV,maxR]
