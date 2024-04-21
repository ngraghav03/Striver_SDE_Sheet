'''
Problem Statement: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    current = head
    while current != None:
        print(current.data, end = " ")
        current = current.next
    print()

def findIntersection(head1, head2):
    
    # ! Step1 : Find the length of the the two lists.
    l1 = 0
    l2 = 0

    current1 = None
    current2 = None

    current = head1
    # print("1: ")
    while current != None:
        l1 += 1
        # print(current.data, end = " ")
        current = current.next
    # print()

    current = head2
    # print("2: ")
    while current != None:
        l2 += 1
        # print(current.data, end = " ")
        current = current.next
    # print()

    # print(l1, l2)

    # ! Step 2: Find the positive difference between l1 and l2
    diff = abs(l1 - l2)
    # print(diff, end = " ")

    # ! Step 3: Move current pointer of the larger list by diff number of positions
    if l1 > l2:
        k1 = 1
        current1 = head1
        while k1 <= diff:
            k1 += 1
            current1 = current1.next
    
        current2 = head2
    
    else:
        k2 = 1
        current2 = head2
        while k2 <= diff:
            k2 += 1
            current2 = current2.next
    
        current1 = head1

    # ! Step 4: Now move both the pointers. If they collide return the colliding node, else move both pointers to next one until end of list.
    # print(current1.data, current2.data)

    while current1 != None and current2 != None:
        if current1 == current2:
            return current1
        current1 = current1.next
        current2 = current2.next

    return head1
    


# Main
head1 = Node(1)
head2 = Node(3)

head1.next = Node(3)
head1.next.next = Node(1)
head1.next.next.next = Node(2)
head1.next.next.next.next = Node(4)

head2.next = head1.next.next.next
printLL(head1)
printLL(head2)

print("The intersection point is: ")
print(findIntersection(head1, head2).data)

# ? Time Complexity: O(M x N) where M and N is the length of the 1st and 2nd linked lists
# ? Space Complexity: O(1) as we are not using any additional space.