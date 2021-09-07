class Node: 
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Height:
    def __init__(self):
        self.h = 0

def diameterOpt(root, height):
    lh = Height()
    rh = Height()

    if root is None:
        height.h = 0
        return 0

    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)

    height.h = max(lh.h, rh.h) + 1

    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))

def diameter(root):
    height = Height()
    return diameterOpt(root, height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))