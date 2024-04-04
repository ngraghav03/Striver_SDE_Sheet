'''
Problem Statement: Given an array of integers A and an integer B. 
Find the total number of subarrays having bitwise XOR of all elements equal to k.
'''

def noOfSubarraysWithXOR_k(array, k):
    n = len(array)
    count = 0

    # Generate subarrays
    for i in range(n):
        for j in range(i, n):

            xorr = 0
            # Calculate XOR of all elements of subarray
            for K in range(i, j + 1):
                xorr = xorr ^ array[K]
            
            # Check if XOR == k, and update count if needed
            if xorr == k:
                count += 1
        
    return count

# Main 
a = [4, 2, 2, 6, 4]
k = 6
print("The number of subarrays with XOR k is:", noOfSubarraysWithXOR_k(a, k))


# ? Time Complexity: O(N^3) as we are using three nested loops
# ? Space Complexity: O(1) as we are not using any additional space.            
