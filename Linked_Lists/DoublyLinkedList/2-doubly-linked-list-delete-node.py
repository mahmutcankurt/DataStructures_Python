import gc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def deleteNode(self, deleted):
        if(self.head == None or deleted == None):
            return

        if(self.head == deleted):
            self.head = deleted.next

        if(deleted.next != None):
            deleted.next.prev = deleted.prev

        if(deleted.prev != None):
            deleted.prev.next = deleted.next

        gc.collect()

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if(self.head != None):
            self.head.prev = new_node

        self.head = new_node

    def printList(self, node):
        while(node != None):
            print(node.data)
            node = node.next

dll = DLL()

dll.push(3)
dll.push(5)
dll.push(9)
dll.push(11)

print("\nOriginal Doubly Linked List: ")
dll.printList(dll.head)

dll.deleteNode(dll.head)
dll.deleteNode(dll.head.next)
dll.deleteNode(dll.head.next)

print("\nModified Doubly Linked List: ")
dll.printList(dll.head)