'''
You are given the root of a binary tree and an integer distance.
A pair of two different leaf nodes of a binary tree is said to be 
good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.
https://www.youtube.com/watch?v=vrbJ7aDuK-A
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        adj = defaultdict(list)
        leaf = set()
        def inorder(root):
            if not root:
                return
            if not root.left and not root.right:
                leaf.add(root)
            if root.left:
                adj[root].append(root.left)
                adj[root.left].append(root)
                inorder(root.left)
            if root.right:
                adj[root].append(root.right)
                adj[root.right].append(root)
                inorder(root.right)

        inorder(root)
        count = 0
        for each in leaf:
            level = 0
            visited = set()
            queue = deque()
            queue.append(each)
            visited.add(each)
            while queue and level<=distance:
                length = len(queue)
                while length>0:
                    node = queue.popleft()
                    if node in leaf and node!=each:
                        count+=1
                    for child in adj[node]:
                        if child not in visited:
                            queue.append(child)
                            visited.add(child)
                    length-=1 
                level+=1
        return count//2
