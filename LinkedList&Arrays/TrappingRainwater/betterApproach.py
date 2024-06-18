'''
Problem Statement: 
Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain.
'''
def findPrefix(arr, n):
    # This takes O(N) time

    prefixMax = [0] * n
    maxTillNow = -1
    for i in range(n):
        maxTillNow = max(maxTillNow, arr[i])
        prefixMax[i] = maxTillNow
    
    return prefixMax

def findSuffix(arr, n):
    # This takes O(N) time

    suffixMax = [0] * n
    maxTillNow = -1
    for i in range(n - 1, -1, -1):
        maxTillNow = max(maxTillNow, arr[i])
        suffixMax[i] = maxTillNow
    
    return suffixMax

def trappingRainwater(arr):
    n = len(arr)
    # This takes O(N) time and O(2N) space
    prefixMax = findPrefix(arr, n)
    suffixMax = findSuffix(arr, n)

    # print(prefixMax)
    # print(suffixMax)
    waterTrapped = 0

    for i in range(n):
        leftMax = prefixMax[i]
        rightMax = suffixMax[i]

        waterTrapped += min(leftMax, rightMax) - arr[i]
    
    return waterTrapped

# Main
A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingRainwater(A))

# ? Time Complexity: O(3N), O(2N) for computing prefixMax and suffixMax arrays and O(N) for calculating water trapped.
# ? Space Complexity: O(2N) as we use two arrays of length N.