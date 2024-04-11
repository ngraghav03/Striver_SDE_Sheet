'''
Problem Statement: Given the head of a singly linked list, return the middle node of the linked list. 
If there are two middle nodes, return the second middle node.
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def middle_Of_LL(head):
    mid = head
    n = 1
    temp = head

    '''while temp is not None:
        
        temp = temp.next
        n += 1
        if (n % 2 == 0):
            mid = mid.next
        if temp is None:
            break

    return mid'''
    
    # We start mid from start. For each two steps taken by the temp node, we move mid by one step.abs
    # Therefore, at the end, mid will point to the middle (present at half of the list) of the list.
     
    while temp is not None:
        if (temp.next is None):
            break
        n += 1
        # print("n = ", n)
        if (n % 2 == 0 and n != 0):
            mid = mid.next
        # print("mid = ", mid.data)
        temp = temp.next
        # print(mid.data, temp.data)
    return mid

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
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("Original Linked List: ")
print_LL(head)

middle = middle_Of_LL(head)
print("Linked List from Middle: ")
print_LL(middle)

# ? Time Complexity: O(N)
# ? Space Complexity: O(1)