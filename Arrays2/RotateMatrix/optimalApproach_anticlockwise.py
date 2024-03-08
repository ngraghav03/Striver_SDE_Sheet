'''
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
'''
''' {{1,2,3},
    {4,5,6},
    {7,8,9}}
Output:
    3 6 9 
    2 5 8 
    1 4 7  
'''
# Intuition: We can see that the first column is the reverse of the first row, 2nd column is the reverse of the 2nd row.
# So we get the anticlockwise rotated matrix by finding the transpose and reversing each column.

def rotateMatrix(matrix):

    m = len(matrix)
    n = len(matrix[0])
    # ! Finding Transpose
    for i in range(m):
        for j in range(i + 1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    print("Transpose: ", matrix)

    # ! Reversing each column   
    for j in range(m):
        start = 0
        end = n - 1

        while start <= end:
            matrix[start][j], matrix[end][j] = matrix[end][j], matrix[start][j]
            start += 1
            end -= 1
    print("Final Matrix: ", matrix)

    return matrix

# Main
# This problem is only meant for square matrices
# matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotatedMatrix = rotateMatrix(matrix)
print("..........\n",rotatedMatrix)

# ? Time Complexity: O(n^2) + O(n^2) ~ O(2*n^2) ~ O(n^2) as we are using two nested loops
# ? Space Complexity: O(1) as we are not using a seperate matrix and changing the given matrix in place.
