'''
Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. 
Assuming there is only one duplicate number, your task is to find the duplicate number.
'''
# TODO: We sort the array first and check which element repeat adjacently

def findDuplicateNumber(array):
    array.sort()

    n = len(array)
    for i in range(n - 1):
        if array[i] == array[i + 1]:
            return array[i]

# Main
array = [1, 3, 4, 2, 2]
print("Array = ", array)
duplicateEle = findDuplicateNumber(array)
print("Duplicate number: ", duplicateEle)

# ? Time Complexity: O(NlogN + N). O(NlogN) to sort the array and O(N) to find the duplicate array.
# ? Space Complexity: O(1) as we are not using any extra space.  