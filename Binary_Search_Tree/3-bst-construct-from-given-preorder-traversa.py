class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getPreIndex():
    return constructTreeUtils.preIndex 

def incrementPreIndex():
    constructTreeUtils.preIndex += 1

def constructTreeUtils(pre, low, high):
    if(low > high):
        return None

    root = Node(pre[getPreIndex()])
    incrementPreIndex()

    if low == high:
        return root

    r_root = -1

    for i in range(low, high + 1):
        if (pre[i] > root.data):
            r_root = i
            break

    if r_root == -1: 
        r_root = getPreIndex() + (high - low)

    root.left = constructTreeUtils(pre, getPreIndex(), r_root - 1)
    root.right = constructTreeUtils(pre, r_root, high)

    return root

def constructTree(pre):
    size = len(pre)
    constructTreeUtils.preIndex = 0
    return constructTreeUtils(pre, 0, size - 1)

def printInorder(root):
    if root is None:
        return
    
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)

pre = [20, 10, 2, 14, 80, 100]

root = constructTree(pre)

print("Inorder Traversal of the Constructed Tree: ")
printInorder(root)