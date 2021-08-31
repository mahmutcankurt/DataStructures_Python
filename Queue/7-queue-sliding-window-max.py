'''
MAXIMUM OF ALL SUBARRAYS OF SIZE k

Algorithm:  

1- Create a deque to store k elements.

2- Run a loop and insert first k elements in the deque. Before inserting the element, check if the element at the back of the queue is smaller than the current element, if it is so remove the element from the back of the deque, until all elements left in the deque are greater than the current element. Then insert the current element, at the back of the deque.

3- Now, run a loop from k to end of the array.

4- Print the front element of the deque.

5- Remove the element from the front of the queue if they are out of the current window.

6- Insert the next element in the deque. Before inserting the element, check if the element at the back of the queue is smaller than the current element, if it is so remove the element from the back of the deque, until all elements left in the deque are greater than the current element. Then insert the current element, at the back of the deque.

7- Print the maximum element of the last window.
'''


from collections import deque

def printMax(arr, n, k):
    Qi = deque()

    for i in range(k):
        while(Qi and arr[i] >= arr[Qi[-1]]):
            Qi.pop()

        Qi.append(i)

    for i in range(k, n):
        print(str(arr[Qi[0]]) + " ", end="")

        while(Qi and Qi[0] <= i - k):
            Qi.popleft()

        while(Qi and arr[i] >= arr[Qi[-1]]):
            Qi.pop()
        
        Qi.append(i)

    print(str(arr[Qi[0]]))

if __name__ == "__main__":
    arr = [13, 2, 79, 91, 58, 90, 57]
    k = 3
    printMax(arr, len(arr), k)