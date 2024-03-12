'''
Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. 
Assuming there is only one duplicate number, your task is to find the duplicate number.
'''
# TODO: We use a linked list to find if there is a cycle and use fast and slow pointers to find the duplicate number

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

def findDuplicateNumber(array):
    # TODO: Write slow and fast pointers as array[0]
    slow = array[0]
    fast = array[0]

    # TODO: Move slow and fast pointers by 1 and 2 steps respectively until they collide
    while(True):
        slow = array[slow]
        fast = array[array[fast]]
        if slow == fast:
            break
    
    # TODO: Redefine fast pointer to array[0] and move fast and slow pointer by 1 step until they collide.
    # TODO: The element at which they collide is the duplicate element.
    fast = array[0]
    while slow != fast:
        slow = array[slow]
        fast = array[fast]
    return slow


# Main
array = [1, 3, 4, 2, 2]
print("Array = ", array)
duplicateEle = findDuplicateNumber(array)
print("Duplicate number: ", duplicateEle)

# ? Time Complexity: O(N). Since we traversed through the array only once.
# ? Space Complexity: O(1).
