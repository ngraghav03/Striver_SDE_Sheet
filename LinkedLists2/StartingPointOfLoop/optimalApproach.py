'''
Problem Statement: Given the head of a linked list that may contain a cycle, return the starting point of that cycle. 
If there is no cycle in the linked list return null.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def startingPointOfLoop(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:    # If both slow and fast meet
            # Move fast to head and move it by one step
            fast = head

            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
    
    return None

# Main
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

loopNode = startingPointOfLoop(head)

if loopNode:
    print("Loop Node detected, starting node of loop is: ", loopNode.data)
else:
    print("No loop detected")


# ? Time Complexity: O(N) as we iterate through the list only once.
# ? Space Complexity: O(N) as we store at most N elements in the hashMap.