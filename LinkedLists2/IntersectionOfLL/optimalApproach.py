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
    
    # ! Take two pointers and point them to head of each list.abs
    # ! Iterate over them. If anyone becomes null, point them to the head of the opposite lists and continue iterating until they collide.

    # ! Basic idea is that, initially we start at two heads.
    # ! When one of pointers reach None, we move it to the head of the other list.
    # ! At this time, the other pointer is 'diff' number of steps away from getting to None,
    # ! where diff is the difference in length of the two lists.

    # ! When the 2nd pointers also reaches None, it goes to the head of the 1st list, but pointer1 would have moven diff steps.
    # ! At this time, we notice that both pointers are pointing to the nodes from which both the linked lists are equal in length.


    p1 = head1
    p2 = head2

    while p1 != p2:
        
        if p1 == None:
            p1 = head2
        else:
            p1 = p1.next
        
        if p2 == None:
            p2 = head1
        else:
            p2 = p2.next
    
    return p1
    # ! If there is no intesection, then both pointers will point to None


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

# ? Time Complexity: O(2*max(M, N)) where M and N is the length of the 1st and 2nd linked lists
# ?                  as in the worst case, both the pointers will traverse the entire list
# ?                  Note that this has the same time complexity as the difference in length approach
# ?                  But, this method is more preferred as it is concise
# ? Space Complexity: O(1) as we are not using any additional space.