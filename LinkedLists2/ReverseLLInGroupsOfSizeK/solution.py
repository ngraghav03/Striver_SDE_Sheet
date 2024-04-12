'''
Problem Statement: Given the head of a singly linked list of `n` nodes and an integer `k`, where k is less than or equal to `n`. 
Your task is to reverse the order of each group of `k` consecutive nodes, 
if `n` is not divisible by `k`, then the last group of remaining nodes should remain unchanged.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print()

def reverseLL(head):

    prev = None
    current = head
    while current is not None:
        front = current.next
        current.next = prev
        prev = current
        current = front
    
    return prev
    
def getKthNodeFromHead(head, K):
    current = head
    k = 1
    while current is not None and k < K:
        current = current.next
        k += 1
    if current == None:
        #If we reached end of linked list before we get to K elements, we return None 
        return None
    return current

def reverseLL_InGroups_Of_SizeK(head, K):
    prevLast = None
    current = head
    LLhead = None
    
    # kthNode = getKthNodeFromHead(current, K)
    while current is not None:
        kthNode = getKthNodeFromHead(current, K)

        if kthNode is not None:
            # If we have successfully found out the kth node from current, we reverse the part
            nextNode = kthNode.next
            kthNode.next = None

            kthNode = reverseLL(current)
            if LLhead is None:
                LLhead = kthNode
            
            if prevLast is None:
                prevLast = head

            if prevLast is not None:
                # If we have already have a reversed part of LL, we connect that part to the current part
                prevLast.next = kthNode

            # Update prevLast to the current node as it is the last node (after reversing -> initially 1st node) of the previous LL part.
            prevLast = current
            current = nextNode
        
        else:
            if prevLast:
                prevLast.next = current

            break

    return LLhead
    
# Main
head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(7)
head.next.next.next.next = Node(9)
head.next.next.next.next.next = Node(2)

# Print the original linked list
print("Original Linked List: ")
printLL(head)

# Reverse the linked list
newHead = reverseLL_InGroups_Of_SizeK(head, 4)

# Print the reversed linked list
print("Reversed Linked List: ")
printLL(newHead)

print(".............")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.next.next.next = Node(10)

# Print the original linked list
print("Original Linked List: ")
printLL(head)

# Reverse the linked list
newHead = reverseLL_InGroups_Of_SizeK(head, 4)

# Print the reversed linked list
print("Reversed Linked List: ")
printLL(newHead)
