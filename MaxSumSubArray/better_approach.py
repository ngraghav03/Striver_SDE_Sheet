'''
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.
'''

'''
If we carefully observe, we can notice that to get the sum of the current subarray we just need to add the current element(i.e. arr[j]) to the sum of the previous subarray i.e. arr[i….j-1].

Assume previous subarray = arr[i……j-1]
current subarray = arr[i…..j]
Sum of arr[i….j] = (sum of arr[i….j-1]) + arr[j]

This is how we can remove the third loop and while moving j pointer, we can calculate the sum.
'''


def MSS_better_approach(array):
    n = len(array)
    max = -10000
    start = 0
    end = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += array[j]
        
            if sum > max:
                max = sum
                start = i
                end = j
        # max = max(max, sum)

    return max, start, end

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(MSS_better_approach(arr))

# ? Time Complexity: O(n^2) as we have two nested loops
# ? Space Complexity : O(1) as we are not using any extra space