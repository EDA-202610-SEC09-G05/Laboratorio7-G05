def put(my_bst, key, value):
    """
    Agrega una nueva pareja llave-valor al árbol binario de búsqueda.
    Si la llave ya existe, se actualiza su valor.
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
