'''
Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, 
and return the head pointer to the reversed list.
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
    
def reverse_LL(head):
        
    stack = []
    tmp = head

    while tmp is not None:
        stack.append(tmp.data)
        tmp = tmp.next

    tmp = head
    while tmp is not None:
        tmp.data = stack.pop()

        tmp = tmp.next

    return head

def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Main
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original Linked List: ")
print_LL(head)

head = reverse_LL(head)
print("Reversed Linked List: ")
print_LL(head)

# ? Time Complexity: O(N) + O(N) ~ O(2N) This is because we traverse the linked list twice: 
# ? once to push the values onto the stack, and once to pop the values and update the linked list. 
# ? Both traversals take O(N) time, hence time complexity  O(2N) ~ O(N).

# ? Space Complexity: O(N) We use a stack to store the values of the linked list, and in the worst case, the stack will have all N values,  
# ? ie. storing the complete linked list.


