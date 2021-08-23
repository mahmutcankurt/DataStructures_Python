class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def merge(self, first, second):
        if(first == None):
            return second
        
        if(second == None):
            return first

        if(first.data < second.data):
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first

        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    def mergeSort(self, tempHead):
        if(tempHead == None):
            return tempHead

        if(tempHead.next == None):
            return tempHead
        
        second = self.split(tempHead)

        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)

        return self.merge(tempHead, second)

    def split(self, tempHead):
        fast = slow = tempHead
        while(True):
            if(fast.next == None):
                break
            
            if(fast.next.next == None):
                break
            
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        if(self.head != None):
            self.head.prev = new_node

        self.head = new_node

    def printList(self, node):
        temp = node

        print("Forward Traversal using next pointer: ")
        while(node != None):
            print(node.data)
            temp = node
            node = node.next

        print("\nBackward Traversal using previous pointer: ")
        while(temp):
            print(temp.data)
            temp = temp.prev

dll = DLL()

dll.push(6)
dll.push(21)
dll.push(5)
dll.push(4)
dll.push(31)
dll.push(11)
dll.push(45)
dll.push(79)

dll.head = dll.mergeSort(dll.head)
print("Linked List After Sorting: ")
dll.printList(dll.head)