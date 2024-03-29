'''
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.
'''

'''
The intuition of the algorithm is not to consider the subarray as a part of the answer if its sum is less than 0. 
A subarray with a sum less than 0 will always reduce our answer and so this type of subarray cannot be a part of the subarray with maximum sum.

Here, we will iterate the given array with a single loop and while iterating we will add the elements in a sum variable. 
Now, if at any point the sum becomes less than 0, we will set the sum as 0 as we are not going to consider any subarray with a negative sum. Among all the sums calculated, we will consider the maximum one.

Thus we can solve this problem with a single loop.
'''

def KadanesAlgo(array):
    sum = array[0]
    maximum = -10000
    print(sum, maximum)
    for i in range(1, len(array)):
        sum += array[i]
        print(sum, maximum)
        if sum < 0:
            sum = 0
        if sum > maximum:
            maximum = sum
        print(sum, maximum)
    return maximum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print("Ans",KadanesAlgo(arr))