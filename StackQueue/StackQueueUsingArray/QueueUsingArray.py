'''
Problem Statement: Implement Queue Data Structure using Array with all functions like pop, push, top, size, etc.
'''
maxSize = 10
class Queue:
    def __init__(self):
        self.queue = [-1] * maxSize
        self.front = -1
        self.rear = -1
    
    def push(self, data):               # Enqueue
        if self.size() == maxSize:
            print("Overflow!")
            return

        self.rear = (self.rear + 1) % maxSize

        if self.front == -1:
            self.front = 0

        self.queue[self.rear] = data

        print(self.front, self.rear, self.queue)
    
    def pop(self):                      # Dequeue
        if self.size() == 0:
            print("Underflow!")
            return
        data = self.queue[self.front]
        self.queue[self.front] = -1
        self.front += 1

        return data
    
    def peek(self):                     
        return self.queue[self.front]
    
    def size(self):
        return self.rear - self.front + 1

# Main
q = Queue()
q.push(4)
q.push(14)
q.push(24)
q.push(34)
print("The peek of the queue before deleting any element", q.peek())
print("The size of the queue before deletion", q.size())
print("The first element to be deleted", q.pop())
print("The peek of the queue after deleting an element", q.peek())
print("The size of the queue after deleting an element", q.size())

# ? Time Comeplexity: O(N) where N is the number of operations performed on the stack.
# ?                   Each operation takes O(1) time as we maintain the index of top with each operation.

# ? Space Complexity: O(N) as we store a maximum of N elements if N operations are performed.