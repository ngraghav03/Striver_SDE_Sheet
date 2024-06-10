'''
Problem Statement: Given a linked list containing "N" head nodes where every node in the linked list contains two pointers:

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

def flattenLL(head):
    if head == None or head.next == None:
        return head
    
    mergedHead = flattenLL(head.next)
    
    return merge(head, mergedHead)

def merge(list1, list2):
    p1 = list1
    p2 = list2

    dummyNode = Node(-1)
    current = dummyNode
    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            current.child = p1
            current = p1
            p1 = p1.child

        else:
            current.child = p2
            current = p2
            p2 = p2.child
        
        current.next = None
    
    if p1 is not None:
        current.child = p1
    else:
        current.child = p2
    
    return dummyNode.child


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
head = Node(5)
head.child = Node(14)

head.next = Node(4)
head.next.child = Node(10)

head.next.next = Node(12)
head.next.next.child = Node(13)
head.next.next.child.child = Node(20)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

print("Initial Linked List")
printInitialLL(head)

newHead = flattenLL(head)

print("Final Linked List")
printFinalLL(newHead)

# ? Time Complexity: O(N x 2M) = O(2MN) where N is the number of horizontal nodes and M is the maximum depth (maximum number of vertical nodes)
# ? Recursion depth is of size N and we call merge() at every recursive call which take O(2M) time at the maximum.
# ? So TC = O(N x 2M) = O(2MN)

# ? Space Complexity : O(N)
# ? We do not use any extra space in merge function, since we are only altering the pointers.
# ? But we take a maximum of N space in recursive stack space.