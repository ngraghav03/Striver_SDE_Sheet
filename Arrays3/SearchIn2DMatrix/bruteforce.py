'''
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. 
The elements of each row are sorted in non-decreasing order. 
Moreover, the first element of a row is greater than the last element of the previous row (if it exists). 
You are given an integer 'target', and your task is to find if it exists in the given 'mat' or not.
'''

# ? Traverse the matrix element by element and check if it is equal to target or not. 

def searchIn_2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    
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

# ? Time Complexity: O(NM) ~ O(N^2) as we use two nested loops.
# ? Space Complexity: O(1) as we are not using any additional space 
