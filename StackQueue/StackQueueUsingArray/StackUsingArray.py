'''
Problem statement: Implement a stack using an array.
'''
maxSize = 1000
class Stack:
    def __init__(self):
        self.stack = [-1] * maxSize
        self.top = -1
    
    def push(self, data):
        if self.size() == maxSize:
            print("Overflow!")
            return
        self.top += 1
        self.stack[self.top] = data
    
    def pop(self):
        if self.size() == 0:
            print("Underflow!")
            return
        data = self.stack[self.top]
        self.stack[self.top] = -1
        self.top -= 1
        return data
    
    def peek(self):
        return self.stack[self.top]
    
    def size(self):
        return self.top + 1

# Main
s = Stack()
s.push(6)
s.push(3)
s.push(7)
print("Top of stack is before deleting any element", s.peek())
print("Size of stack before deleting any element", s.size())
print("The element deleted is", s.pop())
print("Size of stack after deleting an element", s.size())
print("Top of stack after deleting an element", s.peek())

# ? Time Comeplexity: O(N) where N is the number of operations performed on the stack.
# ?                   Each operation takes O(1) time as we maintain the index of top with each operation.

# ? Space Complexity: O(N) as we store a maximum of N elements if N operations are performed.