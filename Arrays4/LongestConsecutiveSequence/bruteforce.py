'''
Problem Statement: You are given an array of 'N' integers. 
You need to find the length of the longest sequence which contains the consecutive elements.
'''

def longestConsecutiveSequence(array):
    n = len(array)
    # longest is initialized to 1 as any element is a consecutive sequence in itself.
    longest = 1
    for i in range(n):
        x = array[i]
        k = 1
        next = x + 1
        # Check if x + 1, x + 2, ... are present in the array 
        # Here k is the number of consecutive elements and next is the next consecutive element to be found.
        while next in array:
            next += 1
            k += 1
        # Update longest
        longest = max(longest, k)

    return longest

# Main
arr = [100, 200, 1, 3, 2, 4]
arr1 = [3, 8, 5, 7, 6]
arr2 = [1,3,5,7]
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr))
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr1))
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr2))

# ? Time Complexity: O(N^2) as we are using two nested loops.
# ? Space Complexity: O(1) as we are not using any extra space.