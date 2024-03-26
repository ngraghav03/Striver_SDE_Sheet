'''
Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. 
Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.
'''

def twoSum_optimal(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return "YES"
            # ! return [left, right] --> Variation 2
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    
    return "NO"
    # ! return [-1, -1] --> Variation 2
        

# Main
target = 14
arr = [2, 6, 5, 8, 11]

target1 = 15
# arr = [2, 6, 5, 8, 11]


print(twoSum_optimal(arr, target))
print(twoSum_optimal(arr, target1))

# ? Time Complexity: O(N) as we are using 1 loop.
# ? Space Complexity: O(1) as we are not using any additional space.