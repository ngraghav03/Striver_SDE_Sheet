'''
Problem Statement: Detect a cycle in Linked List - return true or false
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


# Main
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
# Create a loop
fifth.next = third

if detectCycle(head):
    print("Loop detected in the linked list")
else:
    print("No Loop detected in the linked list")

# ? Time Complexity: O(N), where N is the number of nodes in the linked list. 
# ?                  This is because in the worst-case scenario, the fast pointer, which moves quicker, will either reach the end of the list 
# ?                  (in case of no loop) or meet the slow pointer (in case of a loop) in a linear time relative to the length of the list.


# ? Space Complexity: O(1), as the code uses only constant space (two pointers) irrespective of the linked list's length.