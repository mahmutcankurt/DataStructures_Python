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

    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow")
            return
        else:
            self.top -= 1
            return(self.array.pop())

class SpecialStack(Stack):
    def __init__(self):
        super().__init__()
        self.Min = Stack()

    def push(self, x):
        if(self.isEmpty):
            super().push(x)
            self.Min.push(x)

        else:
            super().push(x)
            y = self.Min.pop()
            self.Min.push(y)

            if(x <= y):
                self.Min.push(x)
            else: 
                self.Min.push(y)
    
    def pop(self):
        x = super().pop()
        self.Min.pop()
        return x

    def getMin(self):
        x = self.Min.pop()
        self.Min.push(x)
        return x

if __name__ == "__main__":
    s = SpecialStack()

    s.push(10)
    s.push(20)
    s.push(30)
    print(s.getMin())
    s.push(5)
    print(s.getMin())