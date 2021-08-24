def Stack():
	stack = []
	return stack


def isEmpty(stack):
	return len(stack) == 0


def push(stack, x):
	stack.append(x)


def pop(stack):
	if(isEmpty(stack)):
		print("Error : Stack is Empty")
	else:
		return stack.pop()

def printNGI(array):
	s = Stack()
	index = 0
	next = 0

	push(s, array[0])

	for i in range(1, len(array), 1):
		next = array[i]

		if(isEmpty(s) == False):

			index = pop(s)

			while(index < next):
				print(str(index) + " -- " + str(next))
				if(isEmpty(s) == True):
					break
				index = pop(s)

			if(index > next):
				push(s, index)

		push(s, next)

	while(isEmpty(s) == False):
		index = pop(s)
		next = -1
		print(str(index) + " -- " + str(next))

array = [12, 14, 22, 4]
printNGI(array)
