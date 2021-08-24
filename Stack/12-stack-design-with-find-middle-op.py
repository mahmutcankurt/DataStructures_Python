class DLLNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0

def createStack():
    s = Stack()
    s.count = 0
    return s

def push(s, new_data):
    new_DLLNode = DLLNode(new_data)
    new_DLLNode.prev = None
    new_DLLNode.next = s.head
    s.count += 1

    if(s.count == 1):
        s.mid = new_DLLNode
    
    else:
        s.head.prev = new_DLLNode
        if((s.count % 2) != 0):
            s.mid = s.mid.prev

    s.head = new_DLLNode

def pop(s):
    if(s.count == 0):
        print("Stack is empty")
        return -1

    head = s.head
    item = head.data
    s.head = head.next

    if(s.head != None):
        s.head.prev = None
    s.count -= 1

    if(s.count == 0):
        s.mid = s.mid.next
    return item

def findMiddle(s):
    if(s.count == 0):
        print("Stack is empty now")
        return -1
    return s.mid.data

if __name__ == "__main__":
    s = createStack()

    push(s, 11)
    push(s, 22)
    push(s, 33)
    push(s, 44)
    push(s, 55)
    push(s, 66)
    push(s, 77)

    print("Item popped is " + str(pop(s)))
    print("Item popped is " + str(pop(s)))
    print("Middle Element is " + str(findMiddle(s)))