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
    
    def reverse(self, head, k):
        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        while(current != None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next != None:
            head.next = self.reverse(next, k)
        return prev

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.push(90)
llist.push(80)
llist.push(70)
llist.push(60)
llist.push(50)
llist.push(40)
llist.push(30)
llist.push(20)
llist.push(10)

print("Given Linked List is:")
llist.printList()
llist.head = llist.reverse(llist.head, 4)

print("\nReversed Linked List is:")
llist.printList()