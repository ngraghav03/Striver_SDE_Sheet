'''
Problem Statement: 
Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain.
'''

def trappingRainwater(arr):
    n = len(arr)
    waterTrapped = 0

    for i in range(n):
        j = i
        leftMax = 0
        rightMax = 0

        # This takes O(N) time
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        j = i
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        
        waterTrapped += min(leftMax, rightMax) - arr[i]
    
    return waterTrapped

A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingRainwater(A))

# ? Time Complexity: O(N^2) as the two inner loops together run for O(N) time and outer loop run for O(N) time
# ? Space Complexity: O(1) as we are not using any extra space.
        
