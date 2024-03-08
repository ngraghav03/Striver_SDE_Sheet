
'''
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
'''

# TODO: Approach: Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of the dummy matrix, 
# TODO: take the second row of the matrix, and put it in the second last column of the matrix and so.
# ! How I did it: 
# ! Take a sample 3x3 matrix and see how the indices/positions of the matrix elements change when rotating and find a pattern/formula that govern them
# ! Eg: matrix[0][0] -> newMatrix[0][2 (i.e., n-1)], matrix[0][1] -> newMatrix[1][2],.. and so on.

def rotateMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    newMatrix = [[0 for i in range(m)] for j in range(n)]
    print(newMatrix)
    lastIndex = n - 1
    for i in range(m):
        for j in range(n):
            # newMatrix[j][n - 1 - i] = matrix[i][j]
            newMatrix[n - 1 - j][i] = matrix[i][j]  # for ANTICLOCKWISE ROTATION
    
    return newMatrix

# Main
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
rotatedMatrix = rotateMatrix(matrix1)
print(rotatedMatrix)

# ? Time Complexity: O(n^2) as we are using two nested loops
# ? Space Complexity: O(n^2) as we are using a seperate matrix