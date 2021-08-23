class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def deleteNode(head_ref, deleted):
    if(head_ref == None or deleted == None):
        return
    
    if(head_ref == deleted):
        head_ref = deleted.next

    if(deleted.next != None):
        deleted.next.prev = deleted.prev
    
    if(deleted.prev != None):
        deleted.prev.next = deleted.next

    return head_ref

def deleteNodeGivenPosition(head_ref, n):
    if(head_ref == None or n <= 0):
        return
    
    current = head_ref
    i=1

    while(current != None and i < n):
        current = current.next
        i = i + 1

    if(current == None):
        return
    
    deleteNode(head_ref, current)

    return head_ref

def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.prev = None
    new_node.next = (head_ref)

    if((head_ref) != None):
        (head_ref).prev = new_node
    
    (head_ref) = new_node
    return head_ref

def printList(head):
    while(head != None):
        print(head.data, end=" ")
        head = head.next

head = None

head = push(head, 6)
head = push(head, 3)
head = push(head, 5)
head = push(head, 9)
head = push(head, 11)
head = push(head, 34)
head = push(head, 45)

print("Doubly Linked List Before Deletion: ")
printList(head)

n = 2

head = deleteNodeGivenPosition(head, n)

print("\nDoubly Linked List After Deletion: ")
printList(head)