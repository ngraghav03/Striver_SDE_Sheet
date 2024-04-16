'''
Problem Statement: Given a linked list and an integer N, 
the task is to delete the Nth node from the end of the linked list and print the updated linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This function prints the node at position k from start of Linked List
def gotoK(head, n):
    k = 1
    current = head
    while k < n:
        k += 1
        current = current.next
    print(current.data)

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print() 

def removeNthNode_fromEndOfLL(head, n):
    # We first find the length L of linked list and remove the node (L - N + 1) where N is the node position from end that we want to remove.
    current = head
    L = 0
    while current != None:
        L += 1
        current = current.next

    print("Remove node at position: ", L - n + 1)
    
    current = head
    # Go to node L - n
    for i in range(1, L - n):
        current = current.next
    print("Node at L - n : ", current.data)

    # Removing the node L - n + 1 from list
    front = current.next.next
    current.next = front

    return head

# Main
head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
print("Original List: ")
printLL(head)
n = 3
newHead = removeNthNode_fromEndOfLL(head, n)
print("List after removing the node at position n = ", n, "from end of the list")
printLL(newHead)
# gotoK(head, 2)

# ? Time Complexity: O(N) + O(N - k) where N is the length of linked list, and k is the position of linked list
# ?                  In the worst case, it takes O(2 * N) time if the node to be removed is at the end of list
# ? Space Complexity: O(1) as we are not using any additional space.