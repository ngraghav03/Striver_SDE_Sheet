'''
Problem Statement: 
Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain.
'''

def trappingRainwater(arr):
    n = len(arr)
    waterTrapped = 0

    left = 0
    right = n - 1

    leftMax = 0
    rightMax = 0

    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= leftMax:
                # Update leftMax
                leftMax = arr[left]
            else:
                waterTrapped += leftMax - arr[left]
                # if arr[left] <= arr[right] and arr[left] >= leftMax, then the minimum among leftMax and rightMax is definitely leftMax
                # Therefore, min(leftMax, rightMax) = leftMax
            
            left += 1
        else:
            if arr[right] > rightMax:
                # Update rightMax
                rightMax = arr[right]
            else:
                waterTrapped += rightMax - arr[right]
                # if arr[right] <= arr[left] and arr[right] >= rightMax, then the minimum among leftMax and rightMax is definitely rightMax
                # Therefore, min(leftMax, rightMax) = rightMax
            
            right -= 1
    
    return waterTrapped

A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingRainwater(A))

# ? Time Complexity: O(N) as we use only one loop.
# ? Space Complexity: O(1) as we are not using any extra space.
        
