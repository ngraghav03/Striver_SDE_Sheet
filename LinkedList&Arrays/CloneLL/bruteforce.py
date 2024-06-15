'''
Problem Statement: 
Given a linked list where every node in the linked list contains two pointers:

"next" which points to the next node in the list.
"random" which points to a random node in the list or "null".
Create a "deep copy" of the given linked list and return it.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def clone(head):

    hashMap = {}
    current = head

    while current is not None:
        newNode = Node(current.data)
        hashMap[current] = newNode
        current = current.next

    current = head
    while current is not None:
        if current.next in hashMap:
            hashMap[current].next = hashMap[current.next]
        else:
            hashMap[current].next = None
        hashMap[current].random = hashMap[current.random]
        
        current = current.next
    
    return hashMap[head]

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()    

# Main
head = Node(7)
head.next = Node(14)
head.next.next = Node(21)
head.next.next.next = Node(28)

# Assigning random pointers
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next
head.next.next.next.random = head.next

print("Initial Linked list")
printLL(head)
print("Cloned Linked list")
newHead = clone(head)
printLL(newHead)

# ? Time Complexity: O(2N), O(N) for getting the hashmap and O(N) for assigning next and random pointers

# ? Space Complexity: O(2N), O(N) for hashMap and O(N) for new cloned nodes