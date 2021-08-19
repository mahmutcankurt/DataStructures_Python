class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def __init__(self):
    self.head = None

def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node

    return head_ref

def kAltReverse(head, k):
    return _kAltReverse(head, k, True)
    
def _kAltReverse(Node, k, b):
    if(Node == None):
        return None

    count = 1
    prev = None
    current = Node
    next = None

    while(current is not None and count <= k):
        next = current.next
        
        if(b == True):
            current.next = prev

        prev = current
        current = next
        count = count + 1
    if(b == True):
        Node.next = _kAltReverse(current, k, not b)
        return prev

    else:
        prev.next = _kAltReverse(current, k, not b)
        return Node

def printList(Node):
    count = 0
    while(Node is not None):
        print(Node.data, end=" ")
        Node = Node.next
        count = count + 1

head = None
i = 20

while(i>0):
    head = push(head, i)
    i = i - 1

print("Given Linked List is ")
printList(head)

head = kAltReverse(head, 4)

print("\nModified Linked List is ")
printList(head)
