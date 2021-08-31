class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)

def printCurrentLevel(root, level):
    if(root == None):
        return
    
    if(level == 1):
        print(root.data, end=" ")
    
    elif(level > 1):
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

def height(node):
    if(node == None):
        return 0

    else:
        leftHeight = height(node.left)
        rightHeight = height(node.right)

        if(leftHeight > rightHeight):
            return leftHeight + 1
        else:
            return rightHeight + 1

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is:")
printLevelOrder(root)