'''
Problem Statement:
Check if the given Linked List is Palindrome
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def checkIfPalindrome(head):
    current = head
    stack = []

    while current is not None:
        stack.append(current.data)
        current = current.next

    current = head
    while current is not None:
        temp = stack.pop()
        if current.data == temp:
            current = current.next
        else:
            return False
    
    return True

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

# Main
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Original List")
printLL(head)

isPalindrome = checkIfPalindrome(head)

if isPalindrome:
    print("It is a palindrome")
else:    
    print("It is not a palindrome")

# ? Time Complexity: O(2N) as we iterate once to store elements on the stack and once again to pop elements from stack.
# ? Space Complexity: O(N) as we store N elements in the stack