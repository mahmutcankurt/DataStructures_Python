class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def identical(self, listb):
        a = self.head
        b = listb.head

        while(a != None and b != None):
            if(a.data != b.data):
                return False

            a = a.next
            b = b.next

        return (a == None and b == None)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

llist1 = LinkedList()
llist2 = LinkedList()

llist1.push(1)
llist1.push(2)
llist1.push(3)

llist2.push(1)
llist2.push(2)
llist2.push(4)

if(llist1.identical(llist2) == True):
    print("Identical ")
else:
    print("Not Identical ")