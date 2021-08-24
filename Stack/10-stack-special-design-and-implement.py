class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100

    def isEmpty(self):
        if(self.top == -1):
            return True
        else:
            return False

    def isFull(self):
        if(self.top == self.max -1):
            return True
        else:
            return False
    
    def push(self, data):
        if(self.isFull()):
            print("Stack Overflow")
            return
        else:
            self.top += 1
            self.array.append(data)