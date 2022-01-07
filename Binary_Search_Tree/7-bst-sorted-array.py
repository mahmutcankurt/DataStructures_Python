class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def sorted_array_to_bst(arr):
    if not arr:
        return None

    mid = (len(arr)) / 2
    root = Node(arr[mid])

    root.left = sorted_array_to_bst(arr[:mid])

    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

def preOrder(node):
    if not node:
        return

    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

arr = [10, 20, 30, 40, 50, 60, 70]
root = sorted_array_to_bst(arr)
print("PreOrder Traversal of Constructed BST: ")
preOrder(root)