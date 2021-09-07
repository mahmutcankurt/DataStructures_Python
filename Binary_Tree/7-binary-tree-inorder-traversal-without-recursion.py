class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def inorder(root):
    current = root
    stack = []
    done = 0

    while True:
        if(current != None):
            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            print(current.data, end="")

            current = current.right

        else:
            break
    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)