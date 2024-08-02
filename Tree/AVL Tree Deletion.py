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
    
def deleteNode(root, key):
    if not root:
        return root
        
    if root.data<key:
        deleteNode(root.right,key)
    elif root.data>key:
        deleteNode(root.left,key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
            
    
    # some data
    
    root.height = 1+max(height(root.left),height(root.right))
    
    diff = height(root.left)-height(root.right)
    
    if diff>1 and root.left.data>key:
        return rightrotate(root)
    elif diff<-1 and root.right.data<key:
        return leftrotate(root)
    elif diff>1 and root.left.data<key:
        root.left = leftrotate(root.left)
        return rightrotate(root)
    elif diff<-1 and root.right.data>key:
        root.right = rightrotate(root.right)
        return leftrotate(root)
    return root
        
