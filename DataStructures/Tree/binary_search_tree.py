from DataStructures.Tree import bst_node as bn

def default_compare(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1
    
def insert_node(root, key, value):
    if root is None:
        return bn.new_node(key, value)

    cmp = default_compare(key, root['key'])

    if cmp == 0:
        root['value'] = value
    elif cmp < 0:
        root['left'] = insert_node(root['left'], key, value)
    else:
        root['right'] = insert_node(root['right'], key, value)

    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def put(my_bst, key, value):
    my_bst['root'] = insert_node(my_bst['root'], key, value)
    return my_bst

def get_node(root, key):
    if root is None:
        return None

    cmp = default_compare(key, root['key'])

    if cmp == 0:
        return root
    elif cmp < 0:
        return get_node(root['left'], key)
    else:
        return get_node(root['right'], key)
    
def get(my_bst, key):
    node = get_node(my_bst['root'], key)
    return node['value'] if node else None

def size_tree(root):
    if root is None:
        return 0
    return root['size']

def size(my_bst):
    return size_tree(my_bst['root'])

