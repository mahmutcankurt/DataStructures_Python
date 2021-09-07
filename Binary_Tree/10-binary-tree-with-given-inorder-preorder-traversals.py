class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def buildTree(inorder, preorder, instart, inend):
    if(instart > inend):
        return None

    tNode = Node(preorder[buildTree.preindex])
    buildTree.preindex += 1

    if(instart == inend):
        return tNode

    inindex = search(inorder, instart,inend,tNode.data)

    tNode.left = buildTree(inorder, preorder, instart, inindex-1)
    tNode.right = buildTree(inorder, preorder, inindex+1, inend)

    return tNode

def search(arr, start, end, value):
    for i in range(start, end+1):
        if(arr[i] == value):
            return i

def printInorder(node):
    if(node == None):
        return

    printInorder(node.left)

    print(node.data)
    printInorder(node.right)

inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preindex = 0

root = buildTree(inorder, preorder, 0, len(inorder) - 1)

print("Inorder Traversal of the Constructed Tree is: ")
printInorder(root)