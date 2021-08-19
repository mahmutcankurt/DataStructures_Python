class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class llist:
    def __init__(self):
        self.head = None 

    def reverse(self, head):

        if head is None or head.next is None:
            return head

        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return rest

    def __str__(self):
        llistStr = ""
        temp = self.head
        while temp:
            llistStr = (llistStr +
                            str(temp.data) + " ")
            temp = temp.next
        return llistStr

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp


llist = llist()
llist.push(98)
llist.push(10)
llist.push(15)
llist.push(23)
llist.push(24)
llist.push(76)
llist.push(13)
 
print("Given linked list")
print(llist)
 
llist.head = llist.reverse(llist.head)
 
print("Reversed linked list")
print(llist)