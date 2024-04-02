'''
Problem Statement: Given an array containing both positive and negative integers, 
we have to find the length of the longest subarray with the sum of all elements equal to zero.
'''

def longestSubarrayWithKSum(array):
    n = len(array)
    # Longest stores the length of longest subarray with the sum of all elements equal to zero.
    longest = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += array[j]

            if sum == 0:
                longest = max(longest, j - i + 1)
    
    return longest

# Main
a = [9, -3, 3, -1, 6, -5]
print(longestSubarrayWithKSum(a))

# ? Time Complexity: O(N^2) as we are using two neste loops.
# ? Space Complexity: O(1) as we are not using any additional space.