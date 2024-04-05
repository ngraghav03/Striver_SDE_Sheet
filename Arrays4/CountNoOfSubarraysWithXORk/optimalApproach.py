'''
Problem Statement: Given an array of integers A and an integer B. 
Find the total number of subarrays having bitwise XOR of all elements equal to k.
'''

# ! We use prefix XOR of elements for this optimal Approach

def noOfSubarraysWithXOR_k(array, k):
    n = len(array)
    count = 0

    # ! This hashmap is used to store prefix XOR values as keys and count of the occurence of these prefix XOR as values
    # ! Initially we append {0:1} into hashmap, because,
    # ! Suppose that a = [4, 2, 2, 5] and k = 4. Then we have 4 (1st element) as a solution.
    # ! Here xr = 4, k = 4. So xr ^ k = 0 should be there in the hashmap, for it to be a solution.
    hashMap = {0: 1}

    # This is used to find the number of subarrays having XOR = k 
    count = 0

    # This variable is used to compute prefix XORs
    xr = 0

    for i in range(n):
        xr = xr ^ array[i]

        # This is the prefix XOR we want in our first elements of the subarray.
        reqdXOR = xr ^ k

        # If this required prefix XOR is present in the hashMap already, then update count to count + hashMap[reqdXOR]
        if reqdXOR in hashMap:
            count += hashMap[reqdXOR]

        # If this prefix XOR is not already found, add it to the hashMap.
        if xr not in hashMap:
            hashMap[xr] = 1
        
        # If this prefix XOR is already found, increment its count (of occurence)
        elif xr in hashMap:
            hashMap[xr] += 1

        # print(hashMap)
        # print(i, count)
    return count

# Main
a = [4, 2, 2, 6, 4]
a1 = [5, 6, 7, 8, 9]
k = 6
k1 = 5
print("The number of subarrays with XOR k is:", noOfSubarraysWithXOR_k(a, k))
print("The number of subarrays with XOR k is:", noOfSubarraysWithXOR_k(a1, k1))

# ? Time Complexity: O(N) + O(N) depending on which map data structure we are using, where N = size of the array.
# ?                  If we use unordered map, it takes O(N) and if use map (ordered), it takes O(NlogN).
# ?                  Note that in case of unordered map, it takes O(N) searching time in worst case.

# ? Space Complexity: O(N) as we are not using any additional space.            
