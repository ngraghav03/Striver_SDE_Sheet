'''
Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, 
and return the head pointer to the reversed list.
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse_LL(head):
    prev = None
    temp = head

    while temp is not None:

        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
            
    return prev

def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Main
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

print("Original Linked List: ")
print_LL(head)

head = reverse_LL(head)
print("Reversed Linked List: ")
print_LL(head)

# ? Time Complexity: O(N) The code traverses the entire linked list once, 
# ? where ‘n’ is the number of nodes in the list. This traversal has a linear time complexity, O(n).

# ? Space Complexity: O(1) The code uses only a constant amount of additional space, regardless of the linked list’s length. 
# ? This is achieved by using three pointers (prev, temp and front) to reverse the list without any significant extra memory usage, 
# ? resulting in constant space complexity, O(1).