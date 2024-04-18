'''Problem Statement: 
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list instead, you will be given access to the node to be deleted directly. 
It is guaranteed that the node to be deleted is not a tail node in the list.
'''
'''
Example:
LL = 1 -> 2-> 3 -> 4 -> 5
Node given to be deleted: 3
New LL = 1 -> 2 -> 4 -> 5
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNodeFromLL(node):

    NodeToBeDeleted = node
    # We copy the node next to the node to be deleted, to the node to be deleted
    NodeToBeDeleted.data = node.next.data
    # We disconnect the node next to the node to be deleted by connecting the node to be deleted (now having the successor data) to 
    # the successor of successor. 
    NodeToBeDeleted.next = node.next.next

def printLL(head):
    current = head
    while current != None:
        print(current.data, end = " ")
        current = current.next
        print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked list:")
printLL(head)

deleteNodeFromLL(head.next.next)

print("Linked list after deleting the node")
printLL(head)

# ? Time Complexity: O(1) as we are not using any loop but just modifying one link and one node data
# ? Space Complexity: O(1) as we are not using any additional space.