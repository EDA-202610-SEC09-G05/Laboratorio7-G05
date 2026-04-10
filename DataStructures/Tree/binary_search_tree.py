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
    """
    Agrega una nueva pareja llave-valor al árbol binario de búsqueda.
    Si la llave ya existe, se actualiza su valor.
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst


