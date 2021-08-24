from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

        self.curr_size = 0

    def push(self, x):
        self.curr_size += 1
        self.q2.put(x)

        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q  = self.q1
        self.q1 = self.q2
        self.q2 = self.q

    def pop(self):
        if(self.q1.empty()):
            return
        self.q1.get()
        self.curr_size -= 1
    
    def top(self):
        if(self.q1.empty()):
            return -1
        return self.q1.queue[0]
    
    def size(self):
        return(self.curr_size)

if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print("Current Size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("Current Size: ", s.size())