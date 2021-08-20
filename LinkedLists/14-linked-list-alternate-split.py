class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AlternateSplit(self, a, b):
        first = self.head
        second = first.next

        while(first != None and second != None and first.next != None):
            self.MoveNode(a, first)
            self.MoveNode(b, second)

            first = first.next.next

            if(first == None):
                break

            second = first.next

    def MoveNode(self, dest, node):
        new_node = Node(node.data)

        if(dest.head == None):
            dest.head = new_node
        else:
            new_node.next = dest.head
            dest.head = new_node

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        
        print("")

if __name__ == "__main__":
    llist = LinkedList()
    a = LinkedList()
    b = LinkedList()

    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.push(0)

    llist.AlternateSplit(a, b)

    print("Original Linked List: ")
    llist.printList()

    print("Resultant Linked List 'a': ")
    a.printList()

    print("Resultant Linked List 'b': ")
    b.printList()