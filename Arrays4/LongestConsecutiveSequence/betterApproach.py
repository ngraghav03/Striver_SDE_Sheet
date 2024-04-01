'''
Problem Statement: You are given an array of 'N' integers. 
You need to find the length of the longest sequence which contains the consecutive elements.
'''

def longestConsecutiveSequence(array):
    n = len(array)
    # longest is initialized to 1 as any element is a consecutive sequence in itself.
    longest = 1
    # We sort the array
    array.sort()
    lastElement = array[0]
    length = 1
    for i in range(1, n):
        if array[i] == lastElement + 1:
            lastElement = array[i]
            length += 1
        
        elif array[i] != lastElement:
            lastElement = array[i]
            length = 1
        
        longest = max(longest, length)

    return longest

# Main
arr = [100, 200, 1, 3, 2, 4]
arr1 = [3, 8, 5, 7, 6]
arr2 = [1,3,5,7]
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr))
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr1))
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr2))

# ? Time Complexity: O(NlogN) + O(N). O(NlogN) for sorting the array, and O(N) as we are using one for loop that runs for (n - 1) times.
# ? Space Complexity: O(1) as we are not using any extra space.