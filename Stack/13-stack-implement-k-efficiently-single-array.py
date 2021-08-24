class KStacks:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.array = [0]  * self.n
        self.top   = [-1] * self.k
        self.free = 0
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    def isEmpty(self, sn):
        return(self.top[sn] == -1)

    def isFull(self):
        return(self.free == -1)

    def push(self, item, sn):
        if(self.isFull()):
            print("Stack Overflow")
            return
        
        insert_at = self.free
        self.free = self.next[self.free]
        self.array[insert_at] = item
        self.next[insert_at] = self.top[sn]
        self.top[sn] = insert_at

    def pop(self, sn):
        if(self.isEmpty(sn)):
            return None
        
        top_of_stack = self.top[sn]
        self.top[sn] = self.next[self.top[sn]]
        self.next[top_of_stack] = self.free
        self.free = top_of_stack

        return self.array[top_of_stack]

    def printStack(self, sn):
        top_index = self.top[sn]
        while(top_index != -1):
            print(self.array[top_index])
            top_index = self.next[top_index]

if __name__ == "__main__":
    kstacks = KStacks(3, 10)

    kstacks.push(15, 2)
    kstacks.push(45, 2)
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)

    print("Popped element from stack 2 is: " + str(kstacks.pop(2)))
    print("Popped element from stack 1 is: " + str(kstacks.pop(1)))
    print("Popped element from stack 0 is: " + str(kstacks.pop(0)))

    kstacks.printStack(0)