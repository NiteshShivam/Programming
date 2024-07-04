'''Given a binary tree, your task is to find all duplicate subtrees from the given binary tree.

Note:  Return the root of each tree in the form of a list array &
the driver code will print the tree in pre-order tree traversal in lexicographically increasing order.
'''
#Approach 1:
class Solution:
    def get(self, mp, node, ans):
        if not node:
            return "N"

        # Construct a unique string representation for the current subtree
        
        left = self.get(mp, node.left, ans) 
        right = self.get(mp, node.right, ans)
        s = left+ ','+right+','+str(node.data)

        # Check if the subtree string exists and its count is 1 (indicating first occurrence)
        if s in mp:
            mp[s]+=1
            if mp[s]==2:
                ans.append(node)

        # Increment the count of the subtree string
        else:
            mp[s] = mp.get(s, 0) + 1

        return s

    def printAllDups(self, root):
        mp = {}  # Hash table to store subtree string counts
        ans = []  # List to store duplicate nodes
        self.get(mp, root, ans)
        ans.sort(key=lambda x:x.data)
        return ans
