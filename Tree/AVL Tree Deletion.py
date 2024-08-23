'''
https://www.geeksforgeeks.org/problems/avl-tree-deletion/1
'''
def height(root):
    if root:
        return root.height
    return 0
def leftrotate(root):
    new_root = root.right
    temp = new_root.left
    root.right = temp
    new_root.left= root
    
    root.height = 1 + max(height(root.left),height(root.right))
    new_root.height = 1+max(height(new_root.left),height(new_root.right))
    return new_root
def rightrotate(root):
    new_root = root.left
    temp =new_root.right
    root.left = temp
    new_root.right  =root
    
    root.height = 1 + max(height(root.left),height(root.right))
    new_root.height = 1+max(height(new_root.left),height(new_root.right))
    return new_root
def getBalance(root):
    if not root:
        return 0
    return height(root.left)-height(root.right)
def getMinimum(root):
    while root.left:
        root = root.left
    return root
def deleteNode(root, key):
    if not root:
        return root
        
    if root.data<key:
        root.right = deleteNode(root.right,key)
    elif root.data>key:
        root.left = deleteNode(root.left,key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = getMinimum(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right,temp.data)
    
    # if not root:
    #     return root
    
    root.height = 1+max(height(root.left),height(root.right))
    
    diff = height(root.left)-height(root.right)
    
    if diff>1 and getBalance(root.left)>=0:
        return rightrotate(root)
    elif diff<-1 and getBalance(root.right)<=0:#root.right.data<key:
        return leftrotate(root)
    elif diff>1 and getBalance(root.left)<0:# root.left.data<key:
        root.left = leftrotate(root.left)
        return rightrotate(root)
    elif diff<-1 and getBalance(root.right)>0:#root.right.data>key:
        root.right = rightrotate(root.right)
        return leftrotate(root)
    return root
        
