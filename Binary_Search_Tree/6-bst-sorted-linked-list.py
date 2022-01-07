class LNode:
    def __init__(self):
        self.data = None
        self.next = None

class TNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

head = None

def sorted_list_to_bst():
    global head

    n = countLNodes(head)
    return sorted_list_to_bst_recur(n)

def sorted_list_to_bst_recur(n):
    global head

    if(n <= 0):
        return None

    left = sorted_list_to_bst_recur(int(n/2))

    root = newNode((head).data)
    root.left = left
    head = (head).next

    root.right = sorted_list_to_bst_recur(n - int(n/2) - 1)

    return root

def countLNodes(head):
    count = 0
    temp = head
    while(temp != None):
        temp = temp.next
        count = count + 1
    
    return count

def push(head, new_data):
    new_node = LNode()
    new_node.data = new_data
    new_node.next = (head)
    (head) = new_node

    return head

def printList(node):
    while(node != None):
        print(node.data, end=" ")
        node = node.next

def newNode(data):
    node = TNode()
    node.data = data
    node.left = None
    node.right = None

    return node

def preOrder(node):
    if(node == None):
        return
    
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)

head = None

head = push(head, 8)
head = push(head, 7)
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)

print("Given Linked List: ")
printList(head)

root = sorted_list_to_bst()
print("\nPreOrder Traversal of Constructed BST: ")
preOrder(root)
