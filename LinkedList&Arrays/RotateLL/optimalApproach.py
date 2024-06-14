'''
Problem Statement: Given the head of a linked list, rotate the list to the right by k places.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotateLL(head, k):
    # ! Step 1: find length of list
    n = 1
    current = head
    while current.next is not None:
        current = current.next
        n += 1
        
    # form a cycle
    current.next = head
    # ! Step 2: find k % n
    k = k % n
    
    # ! Step 3: Disconnect link at (n-k)th position
    p = 1
    current = head
    while p < (n - k):
        current = current.next
        p += 1  

    head = current.next
    current.next = None

    return head


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
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 2

print("Initial Linked List")
printLL(head)
print("Rotated Linked List")
newHead = rotateLL(head, k)
printLL(newHead)

# ? Time Complexity: O(N*k)
# ? Space Complexity: O(1)