'''
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
Write a program to in-place sort the array without using inbuilt sort functions.
( Expected: Single pass-O(N) and constant space)
'''

def sort012Array_Optimal(array):
    low = 0
    mid = 0
    high = len(array) - 1

    while(mid<=high):
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1

        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            array[high], array[mid] = array[mid], array[high]
            high -= 1
    
    return array

# Main
arr = [0, 2, 1, 2, 0, 1, 1]
print(sort012Array_Optimal(arr))

# ? Time Complexity: O(N), where N = size of the given array.
# ? Reason: We are using a single loop that can run at most N times.

# ? Space Complexity: O(1) as we are not using any extra space.