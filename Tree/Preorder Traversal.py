'''
https://www.geeksforgeeks.org/problems/preorder-traversal/1
'''
def p(root,result):
    if not root:
        return 
    result.append(root.data)
    p(root.left,result)
    p(root.right,result)
def preorder(root):
    result = []
    p(root, result)
    return result
