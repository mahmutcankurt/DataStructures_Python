class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def transformTreeUtil(root):
    if root == None:
        return

    transformTreeUtil(root.right)

    global sum
    sum = sum + root.data

    root.data = sum - root.data

    transformTreeUtil(root.left)

def transformTree(root):
    transformTreeUtil(root)

def printInorder(root):
    if root == None:
        return

    printInorder(root.left) 
    print(root.data, end = " ")
    printInorder(root.right)

if __name__ == "__main__":
    sum = 0

    root = Node(12)
    root.left = Node(3)
    root.right = Node(30)
    root.left.left = Node(2)
    root.left.right = Node(8)
    root.right.left = Node(16)
    root.right.right = Node(41)
    root.right.right.left = Node(36)

    print("Inorder traversal of given tree: ")
    printInorder(root)

    transformTree(root)

    print("\nInorder traversal of transformed tree: ")
    printInorder(root)