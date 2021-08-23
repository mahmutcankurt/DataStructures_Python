class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def reverseWithStack(self):
        stack = []
        temp = self.head
        while(temp != None):
            stack.append(temp.data)
            temp = temp.next

        temp = self.head
        while(temp != None):
            temp.data = stack.pop()
            temp = temp.next

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
dll.push(34)
dll.push(45)

print("Original Doubly Linked List: ")
dll.printList(dll.head)

dll.reverseWithStack()

print("\nReversed Doubly Linked List: ")
dll.printList(dll.head)