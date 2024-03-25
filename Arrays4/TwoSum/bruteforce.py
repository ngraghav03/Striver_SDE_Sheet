'''
Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. 
Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.
'''

def twoSum_bruteForce(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return "YES"
                # ! return [i, j] --> Variation 2
    
    return "NO"
    # ! return [-1, -1]

# ? Time Complexity: O(N^2) as we are using 2 nested loops.
# ? Space Complexity: O(1) as we are not using any additional space.