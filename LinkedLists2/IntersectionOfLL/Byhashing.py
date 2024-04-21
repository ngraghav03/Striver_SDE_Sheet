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
    
    # Iterate over list1 and add it to a hashset.
    # Then iterate over list2 and check if that node is present in the hashset.abs

    current1 = head1
    current2 = head2

    hashset = set()
    while current1 != None:
        hashset.add(current1)
        current1 = current1.next
    
    while current2 != None:
        if current2 in hashset:
            return current2
        current2 = current2.next
    
    return None


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

# ? Time Complexity: O(M + N) where M and N is the length of the 1st and 2nd linked lists
# ? Space Complexity: O(M) as we are storing at most M elements in the hashSet.