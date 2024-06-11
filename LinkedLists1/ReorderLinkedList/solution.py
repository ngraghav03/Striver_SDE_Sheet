'''.
Problem Statement:
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Eg:
Input:  1 -> 2 -> 3 -> 4
Output: 1 -> 4 -> 2 -> 3

Input:  1 -> 2 -> 3 -> 4 -> 5
Output: 1 -> 5 -> 2 -> 4 -> 3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLL(head):
    prev = None
    current = head
    while current != None:
        front = current.next
        current.next = prev
        prev = current
        current = front
    
    return prev
    
def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

def reorderList(head):
    # Step 1: Find the middle element of LL
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    middle = slow

    head2 = slow.next
        
    middle.next = None

    head2 = reverseLL(head2)

    pointer1 = head
    pointer2 = head2

    while pointer1 is not None or pointer2 is not None:
        if pointer1 and pointer2:
            next1 = pointer1.next
            next2 = pointer2.next

            pointer1.next = pointer2
            pointer2.next = next1

            pointer1 = next1
            pointer2 = next2
            
        elif pointer1 is not None and pointer2 is None:
            pointer1.next = None
            pointer1 = pointer1.next
    
    return head

# Main

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Initial Linked List")
printLL(head)
print("After reordering, the linked list is")
newHead = reorderList(head)
printLL(newHead)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("Initial Linked List")
printLL(head)
print("After reordering, the linked list is")
newHead = reorderList(head)
printLL(newHead)