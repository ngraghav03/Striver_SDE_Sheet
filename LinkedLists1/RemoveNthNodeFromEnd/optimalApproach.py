'''
Problem Statement: Given a linked list and an integer N, 
the task is to delete the Nth node from the end of the linked list and print the updated linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# This function prints the node at position k from start of Linked List
def gotoK(head, n):
    k = 1
    current = head
    while k < n:
        k += 1
        current = current.next
    print(current.data)

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print() 

def removeNthNode_fromEndOfLL(head, n):

    left = head
    right = head
    # ! Step1 : Move right pointer to position n from start of linked list
    k = 1
    while k < n:
        k += 1
        right = right.next
    
    print("Right: ", right.data)

    # ! Step2 : Move left and right pointer by one step till right reached end of list
    prev = None
    while right.next is not None:
        prev = left
        left = left.next
        right = right.next
    
    # print("prev: ", prev.data, "left: ", left.data)
    # ? If prev is None after this loop, and left and right are same, then it means that the linked list has only one element
        if prev == None:
            if left == right:
                return None
            else:
                # ? If prev is None and if left and right are not same, then it means that there are two elements in the list
                # ? and we need to remove the left element which is the first element
                # ? To remove this element, we return the node at left.next which is the second and last element of the list.
                # ? In case, left is 1st element and there are more than 2 elements, to remove left, we return left.next
                return left.next

        # ! IMPORTANT! Note that we need at least 3 elements in the list for prev to be not None and to connect prev to front of left node.

    # ! Step3: Remove node at left
    front = left.next
    prev.next = front

    return head

# Main
head = Node(0)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(4)
print("Original List: ")
printLL(head)
n = 3
newHead = removeNthNode_fromEndOfLL(head, n)
print("List after removing the node at position n = ", n, "from end of the list")
printLL(newHead)

# ? Time Complexity: O(k) + O(N - k) O(N) where N is the length of linked list, and k is the position of linked list
# ?                  First we move right by k position which take O(k) time, then move right and left by (N - k) positions. So totally, O(N).
# ? Space Complexity: O(1) as we are not using any additional space.