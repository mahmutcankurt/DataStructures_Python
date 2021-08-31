class Queue():
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.back = -1

    def EnQueue(self, data):
        if((self.back + 1) % self.size == self.front):
            print(" Queue is full\n")

        elif(self.front == -1):
            self.front = 0
            self.back = 0
            self.queue[self.back] = data

        else:
            self.back = (self.back + 1) % self.size
            self.queue[self.back] = data

    def DeQueue(self):
        if(self.front == -1):
            print(" Queue is empty\n")

        elif(self.front == self.back):
            temp = self.queue[self.front]
            self.front = -1
            self.back = -1

            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size

            return temp

    def printQueue(self):
        if(self.front == -1):
            print("Queue is empty")

        elif(self.back >= self.front):
            print("Circular Queue's Elements are: ", end=" ")

            for i in range(self.front, self.back + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Circular Queue's Elements are: ", end=" ")

            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.back + 1):
                print(self.queue[i], end=" ")
            print()

        if((self.back + 1) % self.size == self.front):
            print("Queue is Full")

queue = Queue(5)
queue.EnQueue(15)
queue.EnQueue(23)
queue.EnQueue(14)
queue.EnQueue(-7)
queue.EnQueue(67)
queue.EnQueue(76)
queue.printQueue()
print("Deleted value is: ", queue.DeQueue())
print("Deleted value is: ", queue.DeQueue())
queue.printQueue()
queue.EnQueue(10)
queue.EnQueue(21)
queue.EnQueue(6)
queue.printQueue()