'''
Problem Statement: Given a linked list that contains only 1 and 0 return the count of maximum consecutive ones in the list.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMaxConsecutiveOnes(head):
    maxCount = 0
    count = 0
    
    current = head
    while current is not None:
        if current.data == 1:
            count += 1
        else:
            count = 0
        
        maxCount = max(maxCount, count)
        current = current.next

    return maxCount

# Main
A1 = [1,1,0,1,1,1]
head1 = Node(1)
head1.next = Node(1)
head1.next.next = Node(0)
head1.next.next.next = Node(1)
head1.next.next.next.next = Node(1)
head1.next.next.next.next.next = Node(1)

A2 = [1,0,1,1,0,1]
head2 = Node(1)
head2.next = Node(0)
head2.next.next = Node(1)
head2.next.next.next = Node(1)
head2.next.next.next.next = Node(0)
head2.next.next.next.next.next = Node(1)
print(A1, "-> ", findMaxConsecutiveOnes(head1))
print(A2, "-> ", findMaxConsecutiveOnes(head2))

# ? Time Complexity: O(N)
# ? Space Complexity Complexity: O(1)