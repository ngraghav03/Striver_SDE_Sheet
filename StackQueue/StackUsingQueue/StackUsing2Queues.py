'''
Problem Statement: Implement Queue using two stacks
'''
maxSize = 10
class MyStack:
    def __init__(self):
        self.queue = [-1] * maxSize
    
    def push(self, data):               # Enqueue
        if self.size == maxSize:
            print("Overflow!")
            return
        
        self.queue.append(data)
    
    def pop(self):                      # Dequeue
        queue2 = []

        while self.size() != 1:
            poppedEle = self.queue.pop(0)
            queue2.append(poppedEle)

        popEle = self.queue.pop()

        while len(queue2) != 0:
            poppedEle = queue2.pop(0)
            self.push(poppedEle)

        return popEle
    
    def peek(self): 
        queue2 = []

        while self.size() != 1:
            poppedEle = self.queue.pop(0)
            queue2.append(poppedEle)
        
        topEle = self.queue.pop()

        while len(queue2) != 0:
            poppedEle = queue2.pop(0)
            self.push(poppedEle)
        
        self.push(topEle)

        return topEle                   
        
    
    def size(self):
        return len(self.queue)

# Main
s = MyStack()
s.push(3)
s.push(2)
s.push(4)
s.push(1)
print("Top = ", s.peek())
print("Popped Element = ", s.pop())
print("Top = ", s.peek())

# ? Time Complexity : O(N) as pop and peek operation take O(N) time
# ? Space Complexity: O(2N) as we are using 2 queues.