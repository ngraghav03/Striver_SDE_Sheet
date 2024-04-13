'''
Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, 
and return the head pointer to the reversed list.
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse_LL(head):
    if(head == None or head.next == None):
        return head         # 0 or 1 node

    newHead = reverse_LL(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newHead
    


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

# ? Time Complexity: O(N) This is because we traverse the linked list twice: once to push the values onto the stack, 
# ? and once to pop the values and update the linked list. Both traversals take O(N) time.

# ? Space Complexity: O(1) No additional space is used explicitly for data structures or allocations during the linked list reversal process. 
# ? However, it’s important to note that there is an implicit use of stack space due to recursion. 
# ? This recursive stack space stores function calls and associated variables during the recursive traversal and reversal of the linked list. 
# ? Despite this, no extra memory beyond the program’s existing execution space is allocated, hence maintaining a space complexity of O(1).