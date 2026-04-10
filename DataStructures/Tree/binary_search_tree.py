def insert_node(root, key, value):
    if root is None:
        return bst_node(key, value)
    
    if key == root.key:
        root.value = value
    elif key < root.key:
        root.left = insert_node(root.left, key, value)
    else:
        root.right = insert_node(root.right, key, value)
    
    return root

def put(my_bst, key, value):
    
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def get(my_bst, key):

    node = get_node(my_bst['root'], key)
    
    return node['value'] if node else None

def get_node(root, key):
    
    if root is None or root['key'] == key:
        return root
    
    if key < root['key']:
        return get_node(root['left'], key)
    
    return get_node(root['right'], key)

def size(my_bst):
    return size_tree(my_bst['root'])

def size_tree(root):
    if root is None:
        return 0
    return root['size']