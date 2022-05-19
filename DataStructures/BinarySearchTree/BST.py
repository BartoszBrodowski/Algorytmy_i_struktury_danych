class Node():
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def minNode(node):
    currentNode = node
    while currentNode.left is not None:
        # Przerywa gdy znajdzie namniejszy element, czyli
        # ten najbardziej na lewo
        currentNode = currentNode.left
    return currentNode


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)


def delete(root, node):
    if root is None:
        return "Drzewo nie istnieje"
    # Jeśli element jest mniejszy niż korzeń poddrzewa, wchodzimy w lewe poddrzewo
    if node.value < root.value:
        root.left = delete(root.left, node)
    # Jeśli element jest większy niż korzeń poddrzewa, wchodzimy w prawe poddrzewo
    elif node.value > root.value:
        root.right = delete(root.right, node)
    # Gdy element jest równy "korzeniowi", to znaleźliśmy szukany element
    else:
        # Jeśli korzeń ma tylko jedno dziecko, to usuwamy ten korzeń
        # i na jego miejsce wstawiamy to dziecko
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Dwoje dzieci
        temp = minNode(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp)
    return root

# Pierwszy printowany element to element najbardziej
# po lewej stronie drzewa (najmniejszy), a ostatni
# najbardzije po prawej stronie drzewa (największy)


def drukuj_inorder(root):
    if not root:
        return
    drukuj_inorder(root.left)
    print(root.value)
    drukuj_inorder(root.right)


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(60))
drukuj_inorder(r)
# delete(r, Node("bbb"))
# drukuj_inorder(r)
