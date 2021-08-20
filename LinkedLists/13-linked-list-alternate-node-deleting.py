import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteAltNode(head):
    if(head == None):
        return
    
    prev = head
    now = head.next

    while(prev != None and now != None):
        prev.next = now.next
        now = None
        prev = prev.next

        if(prev != None):
            now = prev.next

def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def printList(node):
    while(node != None):
        print(node.data, end=" ")
        node = node.next

if __name__ == "__main__":
    head = None

    head = push(head, 7)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    print("List before calling deleteAltNode() ")
    printList(head)

    deleteAltNode(head)

    print("\nList after calling deleteAltNode() ")
    printList(head)