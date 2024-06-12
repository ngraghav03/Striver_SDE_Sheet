'''
Problem Statement:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def oddEvenList(head):
        
    if head == None or head.next == None:
        return head
    
    oddHead = head
    evenHead = None

    oddPointer = head
    evenPointer = None

    current = head.next
    count = 1

    while current is not None:
        count += 1
        if count % 2 == 0:
            if evenHead is None:
                evenHead = current
                evenPointer = evenHead
            else:
                evenPointer.next = current
                evenPointer = evenPointer.next
            
        else:
            oddPointer.next = current
            oddPointer = oddPointer.next
            
        current = current.next
    
    # Join oddPointer and evenHead
    oddPointer.next = evenHead
    # Remove cycles by assigning None to evenPointer
    evenPointer.next = None
    
    return oddHead

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("Initial Linked List")
printLL(head)
print("After segregating odd and even nodes, the linked list is")
newHead = oddEvenList(head)
printLL(newHead)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Initial Linked List")
printLL(head)
print("After segregating odd and even nodes, the linked list is")
newHead = oddEvenList(head)
printLL(newHead)