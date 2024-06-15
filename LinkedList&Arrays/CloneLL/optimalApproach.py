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

def insertDuplicateInBetween(head):
    current = head

    while current is not None:
        front = current.next

        copyNode = Node(current.data)

        copyNode.next = front

        current.next = copyNode

        current = front
    
    # return head

def connectRandomPointers(head):
    current = head

    while current is not None:
        copyNode = current.next

        if current.random:
            copyNode.random = current.random.next
        else:
            copyNode.random = None
    
        current = current.next.next

def extractCloneLL(head):
    current = head

    dummy = Node(-1)
    pointer = dummy

    while current is not None:
        pointer.next = current.next
        pointer = pointer.next

        current.next = current.next.next
        current = current.next
    
    return dummy.next


def clone(head):
    # Create a clone node and attach it to the original node. Do this for every node
    insertDuplicateInBetween(head)
    printLL(head)
    # Connect random pointers
    connectRandomPointers(head)

    cloneHead = extractCloneLL(head)

    return cloneHead



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