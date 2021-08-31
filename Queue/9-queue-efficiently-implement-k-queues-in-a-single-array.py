class Queue:
    def __init__(self, number_of_queues, array_lenght):
        self.number_of_queues = number_of_queues
        self.array_length = array_lenght
        self.array = [-1] * array_lenght
        self.front = [-1] * number_of_queues
        self.back = [-1] * number_of_queues
        self.next_array = list(range(1, array_lenght))
        self.next_array.append(-1)
        self.free = 0

    def isEmpty(self, queue_number):
        return(True if self.front[queue_number] == -1 else False)

    def isFull(self, queue_number):
        return(True if self.free == -1 else False)

    def EnQueue(self, item, queue_number):
        if(self.isFull(queue_number)):
            print("Queue Full")
            return
        
        next_free = self.next_array[self.free]

        if(self.isEmpty(queue_number)):
            self.front[queue_number] = self.back[queue_number] = self.free
        
        else:
            self.next_array[self.back[queue_number]] = self.free
            self.back[queue_number] = self.free
        
        self.next_array[self.free] = -1
        self.array[self.free] = item
        self.free = next_free

    def DeQueue(self, queue_number):
        if(self.isEmpty(queue_number)):
            print("Queue Empty")
            return
        
        front_index = self.front[queue_number]
        self.front[queue_number] = self.next_array[front_index]
        self.next_array[front_index] = self.free
        self.free = front_index
        return(self.array[front_index])


if __name__ == "__main__":
    q = Queue(3, 10)

    q.EnQueue(15, 2)
    q.EnQueue(45, 2)

    q.EnQueue(17, 1)
    q.EnQueue(49, 1)
    q.EnQueue(39, 1)

    q.EnQueue(11, 0)
    q.EnQueue(9, 0)
    q.EnQueue(7, 0)

    print("Dequeued element from queue 2 is {}".format(q.DeQueue(2)))
    print("Dequeued element from queue 1 is {}".format(q.DeQueue(1)))
    print("Dequeued element from queue 0 is {}".format(q.DeQueue(0)))