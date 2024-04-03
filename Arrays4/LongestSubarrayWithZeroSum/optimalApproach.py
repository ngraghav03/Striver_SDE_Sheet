'''
Problem Statement: Given an array containing both positive and negative integers, 
we have to find the length of the longest subarray with the sum of all elements equal to zero.
'''

# TODO: This problem is used to find subarrays with zero sum, but we can extend this problem for K sum too, by replacing all 0's here with K.

def longestSubarrayWithZeroSum(array):
    n = len(array)
    # Longest stores the length of longest subarray with the sum of all elements equal to zero.
    longest = 1
    
    # This variable is used to calculate the prefix sum of all elements
    sum = 0
    hashMap = {}
    for i in range(n):
        sum += array[i]

        # If sum is 0, then update longest if necessary
        if sum == 0:
            longest = max(longest, i + 1)   # i + 1 is the length of the subarray with sum => len(a[0..i] = i + 1)

        elif sum != 0:
            if sum not in hashMap:
                hashMap[sum] = i
            else:
                # Suppose sum(0..2) = sum(0..5) = k. Then sum(3..5) = 0. Thus, here i = 5, d[sum] = 2. => len(3..5) = 3.
                # So, we use i - d[sum] to get length of that subarray
                longest = max(longest, i - hashMap[sum])

    return longest

# Main
a = [9, -3, 3, -1, 6, -5]
print(longestSubarrayWithZeroSum(a))

# ? Time Complexity: O(N) as we use one loop.
# ? Space Complexity: O(N) as in the worst case we would insert all the array elements prefix sum into our hashMap.