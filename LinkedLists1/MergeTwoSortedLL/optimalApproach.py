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
    prev = None
    newHead = None
    p1 = head1
    p2 = head2
    if p1.data <= p2.data:
        newHead = head1
        prev = p1
        p1 = p1.next
    elif p1.data > p2.data:
        newHead = head2
        prev = p2
        p2 = p2.next

    while p1 is not None and p2 is not None:
        print("prev = ", prev.data)
        print("p1 = ", p1.data)
        print("p2 = ", p2.data)
        if p1.data <= p2.data:
            prev.next = p1
            
            next1 = p1.next
            next2 = p2.next
            
            p1.next = p2
            prev = p2

            p1 = next1
            p2 = next2
        
        elif p1.data > p2.data:
            prev.next = p2

            next1 = p1.next
            next2 = p2.next

            p2.next = p1
            prev = p1

            p1 = next1
            p2 = next2
        
        
    while p1 is None and p2 is not None:
        prev.next = p2
        p2 = p2.next
        prev = prev.next

    while p2 is None and p1 is not None:
        prev.next = p1
        p1 = p1.next
        prev = prev.next
    
    return newHead


def mergeTwoSortedLLs1(head1, head2):
    prev = None
    newHead = None
    p1 = head1
    p2 = head2
    if p1.data <= p2.data:
        newHead = head1
        prev = p1
        p1 = p1.next
    elif p1.data > p2.data:
        newHead = head2
        prev = p2
        p2 = p2.next

    while p1 is not None and p2 is not None:
        # print("prev = ", prev.data)
        # print("p1 = ", p1.data)
        # print("p2 = ", p2.data)
        next1 = p1.next
        next2 = p2.next
        if p1.data <= p2.data:
            prev.next = p1
            prev = prev.next
            p1 = next1

        elif p1.data > p2.data:
            prev.next = p2
            prev = prev.next
            p2 = next2
        
        
    while p1 is None and p2 is not None:
        prev.next = p2
        p2 = p2.next
        prev = prev.next

    while p2 is None and p1 is not None:
        prev.next = p1
        p1 = p1.next
        prev = prev.next
    
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
mergedHead = mergeTwoSortedLLs1(head1, head2)

printLL(mergedHead)

# ? Time Complexity: O(M + N) , where M and N are lengths of linked lists LL1 and LL2
# ?                  as we are traversing pointer1 through entire LL1 and pointer2 through entire LL2.
# ? Time Complexity: O(M + N) as we create a seperate linked list of size M + N to merge the LLs.