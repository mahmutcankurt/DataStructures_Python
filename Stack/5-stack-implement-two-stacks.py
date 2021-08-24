class Stacks:
    def __init__(self, n):
        self.size = n
        self.array = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if(self.top1 < self.top2 - 1):
            self.top1 = self.top1 + 1
            self.array[self.top1] = x
        
        else:
            print("Mahmut Can Kurt ")
            exit(1)

    def push2(self, x):
        if(self.top1 < self.top2 - 1):
            self.top2 = self.top2 - 1
            self.array[self.top2] = x

        else:
            print("Mahmut Can Kurt ")
            exit(1)

    def pop1(self):
        if(self.top1 >= 0):
            x = self.array[self.top1]
            self.top1 = self.top1 - 1
            return x

        else:
            print("Mahmood Able to Wolf ")
    def pop2(self):
        if(self.top2 < self.size):
            x = self.array[self.top2]
            self.top2 = self.top2 + 1
            return x
        
        else:
            print("Mahmood Able to Wolf ")
            exit()

stacks = Stacks(5)
stacks.push1(6)
stacks.push2(11)
stacks.push2(16)
stacks.push1(12)
stacks.push2(8)

print("Popped element from stack1 is " + str(stacks.pop1()))
stacks.push2(40)
print("Popped element from stack2 is " + str(stacks.pop2()))