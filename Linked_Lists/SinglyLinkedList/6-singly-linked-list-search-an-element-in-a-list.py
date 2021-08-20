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

    def search(self, llist, key):
        if(not llist):
            return False
        
        if(llist.data == key):
            return True
            
        return self.search(llist.next, key)


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(5)
    llist.push(6)
    llist.push(98)
    llist.push(3)
    llist.push(1)
    llist.push(10)

    key = 5

    if llist.search(llist.head, key):
        print("Yes!")
    else:
        print("No!")