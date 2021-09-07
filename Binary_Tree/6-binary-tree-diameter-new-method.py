class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def height(root, ans):
    if(root == None):
        return 0

    lh = height(root.left, ans)
    rh = height(root.right, ans)

    ans[0] = max(ans[0], 1 + lh + rh)

    return (1 + max(lh, rh))

def diameter(root):
    if(root == None):
        return 0

    ans = [-999999999999]
    height_of_tree = height(root, ans)
    return ans[0]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(diameter(root))