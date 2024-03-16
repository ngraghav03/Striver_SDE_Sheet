'''
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. 
The elements of each row are sorted in non-decreasing order. 
Moreover, the first element of a row is greater than the last element of the previous row (if it exists). 
You are given an integer 'target', and your task is to find if it exists in the given 'mat' or not.
'''

# ? Imagine that the given 2D matrix is a flattened 1D array of size NM.
# ? We can get the cell number from the given 1D array index and vice versa.abs
# ? 1D index i to cell : (row -> i // m, col -> i % m)
# ? 2D cell number to 1D index i => (m*i + j)  

def searchIn_2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False


# Main
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
target1 = 8
target2 = 17
result1 = searchIn_2DMatrix(matrix, target1)
result2 = searchIn_2DMatrix(matrix, target2)

if result1:
    print(target1, "is present in matrix")
else:
    print(target1, "is not present in matrix")
if result2:
    print(target2, "is present in matrix")
else:
    print(target2, "is not present in matrix")
