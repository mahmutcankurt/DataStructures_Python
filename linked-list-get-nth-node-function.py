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
    
    def getNth(self, llist, position):
        llist.getNthNode(self.head, position, llist)

    def getNthNode(self, head, position, llist):
        count = 0
        if(head):
            if count == position:
                print(head.data)
            else:
                llist.getNthNode(head.next, position - 1, llist)
        else:
            print("Index Doesn't Exist")


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(5)
    llist.push(6)
    llist.push(98)
    llist.push(3)
    llist.push(1)
    llist.push(10)

    print("Element at Index 4 is:", end=" ")
    llist.getNth(llist, 4)