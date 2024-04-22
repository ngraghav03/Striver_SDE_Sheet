'''
Problem Statement: Detect a cycle in Linked List - return true or false
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):
    hashSet = set()
    current = head
    while current != None:
        if current in hashSet:
            return True
        else:
            hashSet.add(current)
    
    return False

# Main
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
# Create a loop
fifth.next = third

if detectCycle(head):
    print("Loop detected in the linked list")
else:
    print("No Loop detected in the linked list")