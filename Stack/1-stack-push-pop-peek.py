class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return True if self.root == None else False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        print("%d pushed to stack" % (data))

    def pop(self):
        if(self.isEmpty()):
            return(float("-inf"))
        
        temp = self.root
        self.root = self.root.next
        popped = temp.data

        return popped

    def peek(self):
        if(self.isEmpty()):
            return(float("-inf"))
        
        return self.root.data

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("%d popped from stack" % (stack.pop()))
print("Top element is % d" % (stack.peek()))