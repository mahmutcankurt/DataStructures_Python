def insert(stack, item):
    if(isEmpty(stack)):
        push(stack, item)
    
    else:
        temp = pop(stack)
        insert(stack, item)
        push(stack, temp)

def reverse(stack):
    if(not isEmpty(stack)):
        temp = pop(stack)
        reverse(stack)
        insert(stack, temp)

def Stack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if(isEmpty(stack)):
        print("Stack is Empty ")
        exit(1)

    return stack.pop()

def printStack(stack):
    for i in range(len(stack) -1, -1, -1):
        print(stack[i], end=" ")
    print()

stack = Stack()

push(stack, str(40))
push(stack, str(30))
push(stack, str(20))
push(stack, str(10))
print("Original Stack is: ")
printStack(stack)

reverse(stack)

print("Reversed Stack is: ")
printStack(stack)