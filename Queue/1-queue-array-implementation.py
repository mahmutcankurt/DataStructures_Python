class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.back = capacity-1
        self.Q = [None]*capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if(self.isFull()):
            print("Full")
            return
        self.back = (self.back + 1) % (self.capacity)
        self.Q[self.back] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    def DeQueue(self):
        if(self.isEmpty()):
            print("Empty")
            return
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def queueFront(self):
        if(self.isEmpty()):
            print("Queue is empty")
        print("Front item is", self.Q[self.front])

    def queueBack(self):
        if(self.isEmpty()):
            print("Queue is empty")
        print("Back item is", self.Q[self.back])

if __name__ == "__main__":
    queue = Queue(30)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.EnQueue(50)
    queue.EnQueue(60)
    queue.EnQueue(70)

    queue.DeQueue()
    queue.queueFront()
    queue.queueBack()