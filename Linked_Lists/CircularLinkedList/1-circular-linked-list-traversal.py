class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        if(self.head != None):
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        
        else:
            ptr1.next = ptr1
        
        self.head = ptr1
    
    def printList(self):
        temp = self.head
        if(self.head != None):
            while(True):
                print(temp.data, end=" ")
                temp = temp.next
                if(temp == self.head):
                    break

cllist = CircularLinkedList()

cllist.push(12)
cllist.push(54)
cllist.push(97)
cllist.push(32)
cllist.push(12)
cllist.push(76)

print("Contents of Circular Linked List")
cllist.printList()