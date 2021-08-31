class Queue:
    def __init__(self):
        self.s = []

    def EnQueue(self, data):
        self.s.append(data)

    def DeQueue(self):
        if(len(self.s) <= 0):
            print("Queue is empty")
            return
        
        x = self.s[len(self.s) -1]
        self.s.pop()

        if(len(self.s) <= 0):
            return x

        item = self.DeQueue()
        self.s.append(x)
        return item

def generate(n):
    q = Queue()
    q.EnQueue("1")

    while(n > 0):
        n -= 1
        s1 = q.DeQueue()
        print(s1)

        s2 = s1

        q.EnQueue(s1 + "0")
        q.EnQueue(s2 + "1")

n = 10
generate(n)