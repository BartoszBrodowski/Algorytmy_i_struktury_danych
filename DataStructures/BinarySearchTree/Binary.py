class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    
def insert(root, key):
    if root == None:
        return Node(key)
    else:
        print(root.value)
        if root.value < key:
            root.right = insert(root.right, key)
        elif root.value > key:
            root.left = insert(root.left, key)
        else:
            return root
    # 50
# 40     60
def printTree(root):
    if root:
        printTree(root.left)
        print(root.value)
        printTree(root.right)

root = Node(50)
root = insert(root, 60)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 80)
root = insert(root, 20)
root = insert(root, 30)


# printTree(root)

