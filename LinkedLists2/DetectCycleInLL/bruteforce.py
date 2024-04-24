'''
Problem Statement: Detect a cycle in Linked List - return true or false
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):
    hashSet = set()
    current = head
    while current != None:
        if current in hashSet:
            return True
        else:
            hashSet.add(current)
    
    return False

# Main
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
# Create a loop
fifth.next = third

if detectCycle(head):
    print("Loop detected in the linked list")
else:
    print("No Loop detected in the linked list")

# ? Time Complexity: O(N * 2 * log(N) )The algorithm traverses the linked list once, 
# ?                  performing hashmap insertions and searches in the while loop for each node. 
# ?                  The insertion and search operations in the unordered_map have a worst-case time complexity of O(log(N)). 
# ?                  As the loop iterates through N nodes, the total time complexity is determined by 
# ?                  the product of the traversal (O(N)) and the average-case complexity of the hashmap operations (insert and search), 
# ?                  resulting in O(N * 2 * log(N)). 

# ? Space Complexity: O(N), The code uses a hashmap/dictionary to store encountered nodes, which can take up to O(N) additional space, 
# ?                   where 'n' is the number of nodes in the list. 
# ?                   Hence, the spacecomplexity is O(N) due to the use of the map to track nodes.