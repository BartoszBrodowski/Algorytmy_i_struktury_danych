class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# def insert(root, key):
#     if root == None:
#         return Node(key)
#     else:
#         if root.value == key:
#             return root
#         elif root.value < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     # TODO Chyba niepotrzebne
#     return root

 
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.value)
#         inorder(root.right)

# root_node = Node(50)
# insert(root_node, 30)
# insert(root_node, 20)
# insert(root_node, 40)
# insert(root_node, 70)
# insert(root_node, 60)
# insert(root_node, 80)

# inorder(root_node)

class BinaryTree:
    def __init__(self, root):
        self.root = None

    def insert(self, root=None, key=None):
        # if self.root == None:
        #     return Node(key)
        if root == None:
            root = self.root
        else:
            if Node(root).value < key:
                root.left = self.insert(root.right, key)
            elif root.value > key:
                root.right = self.insert(root.left, key)
            else:
                return Node(key)

    def print(self, root):
        if root != None:
            print(root.value)
            self.print(root.left)
            self.print(root.right)


drzewko = BinaryTree(Node(50))
drzewko.insert(None, 60)
drzewko.insert(None, 40)
drzewko.print(Node(50))
# drzewko.print(Node(60))


