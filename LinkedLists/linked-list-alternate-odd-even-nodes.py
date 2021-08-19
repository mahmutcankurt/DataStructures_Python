class Node:
    def __init__(self):
        self.data = 0
        self.next = None

def printList(node):
    while(node is not None):
        print(node.data, end=" ")
        node = node.next

    print(" ")

def newNode(key):
    temp = Node()
    temp.data = key
    temp.next = None

    return temp

def insertBegin(head, val):
    temp = newNode(val)
    temp.next = head
    head = temp
    
    return head

def rearrange(head):
    even = None
    temp = None
    prev_temp = None
    i = None
    j = None
    k = None
    l = None
    ptr = None

    temp = (head).next
    prev_temp = head

    while(temp != None):
        x = temp.next

        if(temp.data % 2 != 0):
            prev_temp.next = x
            temp.next = (head)
            (head) = temp
        else:
            prev_temp = temp
        
        temp = x

    temp = (head).next
    prev_temp = (head)

    while(temp != None and temp.data % 2 != 0):
        prev_temp = temp
        temp = temp.next

    even = temp

    prev_temp.next = None

    i = head
    j = even

    while(j != None and i != None):
        k = i.next
        l = j.next
        i.next = j
        j.next = k
        ptr = j
        i = k
        j = l
    
    if(i == None):
        ptr.next = j
    return head

head = newNode(10)
head = insertBegin(head, 9)
head = insertBegin(head, 8)
head = insertBegin(head, 7)
head = insertBegin(head, 6)
head = insertBegin(head, 5)
head = insertBegin(head, 4)
head = insertBegin(head, 3)
head = insertBegin(head, 2)
head = insertBegin(head, 1)

print("Linked List: ")
printList(head)

print("Rearranged Linked List: ")
head = rearrange(head)
printList(head)