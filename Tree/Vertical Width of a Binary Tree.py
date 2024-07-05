'''Given a Binary Tree. You need to find and return the vertical width of the tree.

         1
       /    \
      2      3
     / \    /  \
    4   5  6   7
            \   \
             8   9
 Output: 6 

'''
def verticalWidth(root):
    finalMin = 0
    finalMax = 0
    if not root:
        return 0
    def preorder(root,curr):
        nonlocal finalMin,finalMax
        if not root:
            return
        finalMin = min(finalMin,curr)
        finalMax = max(finalMax,curr)
        if root.left:
            preorder(root.left,curr-1)
        if root.right:
            preorder(root.right,curr+1)
        # code here
    preorder(root,0)
    return abs(finalMin)+abs(finalMax)+1
