'''
Problem Statement: Given two singly linked lists that are sorted in increasing order of node values, 
merge two sorted linked lists and return them as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeTwoSortedLLs(head1, head2):
    newHead = None
    current = None
    pointer1 = head1
    pointer2 = head2

    while pointer1 is not None and pointer2 is not None:
        if pointer1.data <= pointer2.data:
            if newHead is None:
                newHead = Node(pointer1.data)
                current = newHead
            else:
                current.next = Node(pointer1.data)
                current = current.next
            pointer1 = pointer1.next

        else:
            if newHead is None:
                newHead = Node(pointer2.data)
                current = newHead
            else:
                current.next = Node(pointer2.data)
                current = current.next
            pointer2 = pointer2.next

    while pointer1 is not None:
        current.next = Node(pointer1.data)
        current = current.next
        pointer1 = pointer1.next

    while pointer2 is not None:
        current.next = Node(pointer2.data)
        current = current.next
        pointer2 = pointer2.next

    return newHead

def printLL(head):
    current = head
    while current != None:
        print(current.data, end = " ")
        current = current.next
    
# Main
head1 = Node(3)
head1.next = Node(7)
head1.next.next = Node(10)

head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(5)
head2.next.next.next = Node(8)
head2.next.next.next.next = Node(9)

print("Merged Linked Lists:")
mergedHead = mergeTwoSortedLLs(head1, head2)

printLL(mergedHead)

# ? Time Complexity: O(M + N) , where M and N are lengths of linked lists LL1 and LL2
# ?                  as we are traversing pointer1 through entire LL1 and pointer2 through entire LL2.
# ? Time Complexity: O(M + N) as we create a seperate linked list of size M + N to merge the LLs.