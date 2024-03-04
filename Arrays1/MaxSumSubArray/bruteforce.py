'''
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.
'''
# Max sum subarray

def MSS_brute_force(array):
    n = len(array)
    max = -10000
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += array[k]
            
            if sum > max:
                max = sum
            # max = max(max, sum)

    return max

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(MSS_brute_force(arr))

# ? Time Complexity : O(n^3) as we are using 3 nested loops
# ? Space Complexity : O(1) as we are not using any extra space
