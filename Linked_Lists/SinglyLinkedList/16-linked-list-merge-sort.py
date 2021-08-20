class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def mergeSort(head):
    if(head.next == None):
        return head
    
    mid = findMid(head)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)
    finalHead = merge(newHead1, newHead2)

    return finalHead

def merge(head1, head2):
    merged = Node(-1)

    temp = merged

    while(head1 != None and head2 != None):
        if(head1.data < head2.data):
            temp.next = head1
            head1 = head1.next

        else:
            temp.next = head2
            head2 = head2.next

        temp = temp.next

    while(head1 != None):
        temp.next = head1
        head1 = head1.next
        temp = temp.next

    while(head2 != None):
        temp.next = head2
        head2 = head2.next
        temp = temp.next

    return merged.next

def findMid(head):
    slow = head
    fast = head.next

    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow

def printList(head):
    while(head != None):
        print(head.data, end=" ")
        head = head.next

head = Node(7)
temp = head
temp.next = Node(10)
temp = temp.next

temp.next = Node(5)
temp = temp.next

temp.next = Node(20)
temp = temp.next

temp.next = Node(3)
temp = temp.next

temp.next = Node(2)
temp = temp.next

head = mergeSort(head)
print("\nSorted Linked List is: ")
printList(head)