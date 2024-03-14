'''
Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).
What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].
'''

def countInversions(array):
    inversions = 0
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[j] < array[i]:
                print(i, j)
                inversions += 1
    
    return inversions

# Main
array = [1,2,3,4,5]
array1 = [2,1,4,3,5]

print(countInversions(array1))

# ? Time Complexity: O(n^2) as we have two nested loops
# ? Space Complexity: O(1) as we have only one variable storing the count.