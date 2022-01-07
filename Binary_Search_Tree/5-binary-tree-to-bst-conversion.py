class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def storeInorder(root, inorder):
    if(root == None):
        return

    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)

def countNodes(root):
    if(root == None):
        return 0

    return countNodes(root.left) + countNodes(root.right) + 1

def array_to_bst(arr, root):
    if(root == None):
        return

    array_to_bst(arr, root.left)

    root.data = arr[0]
    arr.pop(0)

    array_to_bst(arr, root.right)

def binaryTree_to_bst(root):
    if(root == None):
        return

    n = countNodes(root)
    arr = []
    storeInorder(root, arr)
    arr.sort()
    array_to_bst(arr, root)

def printInorder(root):
    if(root == None):
        return

    printInorder(root.left)
    print(root.data)
    printInorder(root.right)

root = Node(20)
root.left = Node(60)
root.right = Node(30)
root.left.left = Node(40)
root.right.right = Node(10)

binaryTree_to_bst(root)

print("Following is the inorder traversal of the converted BST: ")
printInorder(root)