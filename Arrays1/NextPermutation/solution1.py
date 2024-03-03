'''
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).
'''

def findBreakPoint(permutation):
    n = len(permutation)
    for i in range(n - 2, -1, -1):
        if permutation[i] < permutation[i + 1]:
            return i
    return -1

def swap(breakpoint, permutation):
    n = len(permutation)
    suitableElement = 10000000
    swapIndex = -1
    for i in range(breakpoint + 1, n):
        if permutation[breakpoint] <= permutation[i]:
            if suitableElement > permutation[i]:
                suitableElement = permutation[i]
                swapIndex = i

    permutation[breakpoint], permutation[swapIndex] = permutation[swapIndex], permutation[breakpoint]
    return permutation

    # ? Another method: Since the right half of the permutation is descending, 
    # ? we need fewer iterations to get to the smallest element greater than our arr[breakpoint]
    
def reverseRightHalf(breakpoint, permutation):
    # n = len(permutation)
    # startIndex = breakpoint + 1
    # endIndex = n - 1

    # for i in range(breakpoint + 1, ((n - 1 + breakpoint)//2)):
    #     permutation[i], permutation

    rightHalf = permutation[breakpoint + 1:]
    rightHalf.reverse()
    permutation = permutation[:breakpoint + 1] + rightHalf

    return permutation

def findNextPermutation(permutation):
    i = findBreakPoint(permutation)
    if i == -1:
        return permutation.reverse()
    else:
        # Swap() function swaps the breakpoint with the smallest number greater than arr[breakpoint] in the right side of the breakpoint.
        permutation = swap(i, permutation)
        # Reverse the right half of the permutation
        permutation = reverseRightHalf(i, permutation)

        return permutation


#Main
# arr = eval(input())
permutation = eval(input())
# if permutation in arr:
nextPermutation = findNextPermutation(permutation)
print(nextPermutation)

# ? Time Complexity: O(3N), where N = size of the given array
# ? Finding the break-point, finding the next greater element, and reversal at the end takes O(N) for each, 
# ? where N is the number of elements in the input array. This sums up to 3*O(N) which is approximately O(3N).

# ? Space Complexity: Since no extra storage is required. Thus, its space complexity is O(1).