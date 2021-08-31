from typing import Deque


class Node:
    def __init__(self):
        self.data = None
        self.link = None

class Queue:
    def __init__(self):
        front = None
        back = None

def EnQueue(q, value):
    temp = Node()
    temp.data = value

    if(q.front == None):
        q.front = temp

    else:
        q.back.link = temp

    q.back = temp
    q.back.link = q.front

def DeQueue(q):
    if(q.front == None):
        print("Queue is empty")
        return -999999999999

    value = None
    if(q.front == q.back):
        value = q.front.data
        q.front = None
        q.back = None
    
    else:
        temp = q.front
        value = temp.data
        q.front = q.front.link
        q.back.link = q.front

    return value

def printQueue(q):
    temp = q.front
    print("Circular Queue's Elements are: ", end=" ")

    while(temp.link != q.front):
        print(temp.data, end=" ")
        temp = temp.link
    
    print(temp.data)

if __name__ == "__main__":
    q = Queue()
    q.front = q.back = None

    EnQueue(q, 15)
    EnQueue(q, 23)
    EnQueue(q, 7)

    printQueue(q)

    print("Deleted value: ", DeQueue(q))
    print("Deleted value: ", DeQueue(q))

    printQueue(q)

    EnQueue(q, 10)
    EnQueue(q, 21)
    printQueue(q)