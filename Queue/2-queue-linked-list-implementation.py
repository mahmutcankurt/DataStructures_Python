class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.back = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)

        if(self.back == None):
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp

    def DeQueue(self):
        if(self.isEmpty()):
            return
        temp = self.front
        self.front = temp.next
        
        if(self.front == None):
            self.back = None

if __name__ == "__main__":
    queue = Queue()

    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.DeQueue()
    queue.DeQueue()
    queue.EnQueue(40)
    queue.EnQueue(50)
    queue.EnQueue(60)
    queue.DeQueue()

    print("Queue Front " + str(queue.front.data))
    print("Queue Back " + str(queue.back.data))