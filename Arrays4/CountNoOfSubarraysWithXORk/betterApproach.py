'''
Problem Statement: Given an array of integers A and an integer B. 
Find the total number of subarrays having bitwise XOR of all elements equal to k.
'''

# ! We eliminate one for loop by maintaining XOR value till previous iteration and only updating it in each iteration
# ! and not finding the XOR of subarray from beginning every time.

def noOfSubarraysWithXOR_k(array, k):
    n = len(array)
    count = 0

    # Generate subarrays
    for i in range(n):

        xorr = 0
        for j in range(i, n):
            # XOR[i...j] = XOR[i...j - 1] ^ arr[j]
            xorr = xorr ^ array[j]
            
            # Check if XOR == k, and update count if needed
            if xorr == k:
                count += 1
        
    return count

# Main
a = [4, 2, 2, 6, 4]
k = 6
print("The number of subarrays with XOR k is:", noOfSubarraysWithXOR_k(a, k))
# ? Time Complexity: O(N^2) as we are using two nested loops
# ? Space Complexity: O(1) as we are not using any additional space.            
