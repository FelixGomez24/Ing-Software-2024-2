class TreeNode:
    def __init__(self, value):
        """
        Inicializa un nuevo nodo para un árbol binario.

        Parameters:
            value: El valor del nodo.
        """
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        """
        Inicializa un nuevo árbol binario de búsqueda.
        """
        self.root = None

    def insert(self, value):
        """
        Inserta un nuevo valor en el árbol.

        Parameters:
            value: El valor a insertar en el árbol.
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """
        Inserta recursivamente un nuevo valor en el árbol.

        Parameters:
            node: El nodo actual en el que se está insertando.
            value: El valor a insertar en el árbol.
        """
        if value <= node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def pre_order_traversal(self):
        """
        Realiza un recorrido de preorden en el árbol.

        Returns:
            Una lista de valores en el recorrido de preorden.
        """
        return self._pre_order_recursively(self.root, [])

    def _pre_order_recursively(self, node, result):
        """
        Realiza un recorrido de preorden en el árbol recursivamente.

        Parameters:
            node: El nodo actual en el que se está realizando el recorrido.
            result: La lista que contiene los valores del recorrido.

        Returns:
            Una lista de valores en el recorrido de preorden.
        """
        if node:
            result.append(node.value)
            self._pre_order_recursively(node.left, result)
            self._pre_order_recursively(node.right, result)
        return result

    def in_order_traversal(self):
        """
        Realiza un recorrido de inorden en el árbol.

        Returns:
            Una lista de valores en el recorrido de inorden.
        """
        return self._in_order_recursively(self.root, [])

    def _in_order_recursively(self, node, result):
        """
        Realiza un recorrido de inorden en el árbol recursivamente.

        Parameters:
            node: El nodo actual en el que se está realizando el recorrido.
            result: La lista que contiene los valores del recorrido.

        Returns:
            Una lista de valores en el recorrido de inorden.
        """
        if node:
            self._in_order_recursively(node.left, result)
            result.append(node.value)
            self._in_order_recursively(node.right, result)
        return result

    def post_order_traversal(self):
        """
        Realiza un recorrido de postorden en el árbol.

        Returns:
            Una lista de valores en el recorrido de postorden.
        """
        return self._post_order_recursively(self.root, [])

    def _post_order_recursively(self, node, result):
        """
        Realiza un recorrido de postorden en el árbol recursivamente.

        Parameters:
            node: El nodo actual en el que se está realizando el recorrido.
            result: La lista que contiene los valores del recorrido.

        Returns:
            Una lista de valores en el recorrido de postorden.
        """
        if node:
            self._post_order_recursively(node.left, result)
            self._post_order_recursively(node.right, result)
            result.append(node.value)
        return result

def contar_valles(caminata):
    """
    Cuenta el número de valles en una secuencia de caminata.

    Parameters:
        caminata (str): La secuencia de caminata que contiene 'U' para subida y 'D' para bajada.

    Returns:
        int: El número de valles en la caminata.
    """
    nivel = 0  # Nivel del mar
    valles = 0  # Contador de valles
    en_valle = False  # Indicador si está en un valle

    for paso in caminata:
        if paso == 'U':  # Subiendo
            nivel += 1
            if nivel == 0 and en_valle:
                valles += 1
                en_valle = False
        else:  # 'D' bajando
            nivel -= 1
            if nivel < 0 and not en_valle:
                en_valle = True

    return valles

if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for elem in elements:
        bst.insert(elem)

    caminatas_ejemplo = ["UUUDDDDDU", "DUUUDDDUDUDUUD", "DUUUDDDDUDUDUUD", "UUDUDUDUD", "DDUDUDUUDDUDUDUU"]

    for caminata in caminatas_ejemplo:
        print(f"Analizando caminata: {caminata}")
        valles = contar_valles(caminata)
        print(f"Total de valles: {valles}")

    # Recorridos del árbol binario de búsqueda
    print("Pre-order traversal:", bst.pre_order_traversal())
    print("In-order traversal:", bst.in_order_traversal())
    print("Post-order traversal:", bst.post_order_traversal())

