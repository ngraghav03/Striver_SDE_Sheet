'''
Problem Statement: Given the head of a singly linked list, return the middle node of the linked list. 
If there are two middle nodes, return the second middle node.
'''

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def middle_Of_LL(head):
    n = 0
    temp = head
    while temp is not None:
        n += 1
        temp = temp.next
    # print("n = ", n)
    m = n//2
    # print("Mid value: ",m)
    
    temp = head
    for i in range(m):
        # print(i)
        temp = temp.next
    # print("Final mid data: ",temp.data)
    return temp

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
# head.next.next.next.next.next = Node(6)

print("Original Linked List: ")
print_LL(head)

middle = middle_Of_LL(head)
print("Linked List from Middle: ")
print_LL(middle)
# print(middle.data)

# ? Time Complexity: O(N) + O(N/2) ~ O(3N/2) . The first O(N) is for finding the number of elements in the linked list.
# ? The O(N/2) is to locate the middle element of the linked list

# ? Space Complexity: O(1) as we are not using any additional space.