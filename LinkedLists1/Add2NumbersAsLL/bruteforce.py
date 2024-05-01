'''
Problem Statement: Given the heads of two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Example:
342 + 465 = 807
    2 -> 4 -> 3 
+   5 -> 6 -> 4
-------------------
    7 -> 0 -> 8
-------------------
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addTwoLL(head1, head2):
    # ! For 342 + 465, we add 2 + 5 and pass the carry over to 4 + 6.
    # ! To accomplish this in the linked list, we first add the two heads and update the carry, 
    # ! then move to the next nodes and add the carry and the next two numbers.

    if head1 == None and head2 != None:
        return head2

    if head2 == None and head1 != None:
        return head1 

    carry = 0
    p1 = head1
    p2 = head2

    newHead = None
    pointer = None

    while p1 is not None or p2 is not None:
        val = 0
        if p1 is not None and p2 is not None:
            val = p1.data + p2.data + carry
            p1 = p1.next
            p2 = p2.next

        elif p1 is not None and p2 is None:
            val = p1.data + carry
            p1 = p1.next

        elif p2 is not None and p1 is None:
            val = p2.data + carry
            p2 = p2.next

        carry = val // 10
        val = val % 10
        newNode = Node(val)
        if newHead is None:
            newHead = newNode
            pointer = newHead
        else:
            pointer.next = newNode
            pointer = pointer.next

        

    # if there is a carry after most significant value addition, add 1 to the end of list
    if carry == 1:
        newNode = Node(1)
        pointer.next = newNode
    
    return newHead

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

# Main
head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)
printLL(head1)
printLL(head2)
print("Adding: ")
newHead = addTwoLL(head1, head2)
printLL(newHead)
