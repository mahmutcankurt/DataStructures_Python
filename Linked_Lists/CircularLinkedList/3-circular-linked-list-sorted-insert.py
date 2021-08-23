class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        print(temp.data)
        temp = temp.next
        while(temp != self.head):
            print(temp.data)
            temp = temp.next

    def sortedInsert(self, new_node):
        current = self.head

        if(current == None):
            new_node.next = new_node
            self.head = new_node
        
        elif(current.data >= new_node.data):
            while(current.next != self.head):
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

        else:
            while(current.next != self.head and current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

array = [13, 57, 3, 12, 1, 90]

list_size = len(array)

start = LinkedList()

for i in range(list_size):
    temp = Node(array[i])
    start.sortedInsert(temp)

start.printList()