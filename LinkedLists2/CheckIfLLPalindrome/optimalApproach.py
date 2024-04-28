'''
Problem Statement:
Check if the given Linked List is Palindrome
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLL(head):
    prev = None
    current = head
    while current is not None:
        front = current.next
        current.next = prev
        prev = current
        current = front
    
    return prev

def checkIfPalindrome(head):
    
    # Find the middle of LL
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # head2 is the head of 2nd part of LL
    head2 = slow.next
    reversedHead2 = reverseLL(head2)
    
    slow.next = None

    # Compare the two LL
    p1 = head
    p2 = reversedHead2

    while p1 is not None or p2 is not None:
        if p1 is not None and p2 is not None:
            if p1.data == p2.data:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        
        if p2 is None and p1 is not None:
            p1 = p1.next

    return True


def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

# Main
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Original List")
printLL(head)

isPalindrome = checkIfPalindrome(head)
# printLL(isPalindrome)


if isPalindrome:
    print("It is a palindrome")
else:    
    print("It is not a palindrome")

# ? Time Complexity: O(N/2) + O(N/2) + O(N) as 1st O(N/2) is for finding middle element, 2nd O(N/2) is for reversing 2nd half of list
# ?                  Then, the entire list is traversed once with head1 and head2 traversing N/2 elements each.
# ? Space Complexity: O(1) as we dont use any additional space.