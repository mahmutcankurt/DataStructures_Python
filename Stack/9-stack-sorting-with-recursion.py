def insert(s, element):
    if(len(s) == 0 or element > s[-1]):
        s.append(element)
        return

    else:
        temp = s.pop()
        insert(s, element)
        s.append(temp)

def sorting(s):
    if(len(s) != 0):
        temp = s.pop()
        sorting(s)
        insert(s, temp)

def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()

if __name__ =="__main__":
    s = []
    s.append(31)
    s.append(-6)
    s.append(19)
    s.append(14)
    s.append(-4)

    print("Stack elements before sorting: ")
    printStack(s)

    sorting(s)

    print("\nStack elements after sorting: ")
    printStack(s)

    