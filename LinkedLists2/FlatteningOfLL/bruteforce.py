'''
Problem Statement: Given a linked list containing " N" head nodes where every node in the linked list contains two pointers:

"Next" points to the next node in the list
"Child" pointer to a linked list where the current node is the head
Each of these child linked lists is in sorted order and connected by a 'child' pointer. Your task is to flatten this linked list such that all nodes appear in a single layer or level in a 'sorted order'.

Eg:
3 -> 2 -> 1 -> 4 -> 5
     |    |    |    |
     10   7    9    6
          |    |    |
          11        8
          |
          12

Output:
1
|
2
|
3
...
|
12

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


def traverse(head):
    arr = []
    current = head
    
    while current is not None:
        downpointer = current
        
        while downpointer is not None:
            arr.append(downpointer.data)
            downpointer = downpointer.child
        
        current = current.next

    return arr

def convertArrtoLinkedList(arr):
    n = len(arr)
    if n == 0:
        return None
    
    head = Node(arr[0])
    current = head

    for i in range(1, n):
        current.child = Node(arr[i])
        current = current.child
    
    return head


def flattenLL(head):
    # Step 1: Traverse the LL
    arr = traverse(head)

    # Step 2: Sort the array containing list elements
    arr.sort()

    # Step 3: Create a flattened list from the sorted array
    newHead = convertArrtoLinkedList(arr)

    return newHead

def printFinalLL(head):
    current = head
    while current != None:
        print(current.data, end = " ")
        current = current.child
    
    print()

def printInitialLL(head):
    current = head
    while current is not None:
        downpointer = current
        
        while downpointer is not None:
            print(downpointer.data, end = " ")
            downpointer = downpointer.child
        print("|\n")
        current = current.next

# MAIN
# ! NOTE: This algorithm will work even if the vertical lists are not unsorted as we sort all the elements together in the array.
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

print("Initial Linked List")
printInitialLL(head)

newHead = flattenLL(head)

print("Initial Linked List")
printFinalLL(newHead)

# ? Time Complexity: O(N*M) + O(N*M log(N*M)) + O(N*M) where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointer.

# ? O(N*M) as we traverse through all the elements, iterating through ‘N’ nodes along the next pointer and ‘M’ nodes along the child pointer.
# ? O(N*M log(N*M)) as we sort the array containing N*M (total) elements.
# ? O(N*M) as we reconstruct the linked list from the sorted array by iterating over the N*M elements of the array.


# ? Space Complexity : O(N*M) + O(N*M)where N is the length of the linked list along the next pointer and M is the length of the linked list along the child pointer.

# ? O(N*M) for storing all the elements in an additional array for sorting.
# ? O(N*M) to reconstruct the linked list from the array after sorting