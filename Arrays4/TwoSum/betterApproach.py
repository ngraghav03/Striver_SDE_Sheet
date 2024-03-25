'''
Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. 
Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.
'''

def twoSum(arr, target):
    d = {}
    n = len(arr)
    for i in range(n):
        if (target - arr[i]) in d:
        # if d.has_key(target - arr[i]):
            return "YES"
            # ! return [i, d[target - arr[i]]] --> Variation 2
        else:
            d[arr[i]] = i
            
    return "NO"
    # ! return [-1, -1] --> Variation 2


# Main
target = 14
arr = [2, 6, 5, 8, 11]

target1 = 15
# arr = [2, 6, 5, 8, 11]


print(twoSum(arr, target))
print(twoSum(arr, target1))

# ? Time Complexity: O(N) as we are using only loops.
# ?                   In the worst case(which rarely happens), the unordered_map takes O(N) to find an element. 
# ?                   In that case, the time complexity will be O(N^2). If we use map instead of unordered_map, 
# ?                   the time complexity will be O(N* logN) as the map data structure takes logN time to find an element.

# ? Space Complexity: O(N) as we are store at most N key-value pairs.