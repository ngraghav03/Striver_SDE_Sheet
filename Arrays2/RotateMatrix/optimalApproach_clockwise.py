
'''
Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
'''
# Intuition: By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix, 
# so that’s why we transpose the matrix and then reverse each row, 
# and since we are making changes in the matrix itself space complexity gets reduced to O(1).

def rotateMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    # newMatrix = [[0 for i in range(m)] for j in range(n)]
    # lastIndex = n - 1
    # for i in range(m):
    #     for j in range(n):
    #         newMatrix[j][n - 1 - i]= matrix[i][j]

    # ! To get the transpose of the matrix, we interchange matrix[i][j] with matrix[j][i] only when i<=j. 
    # ! We impose this condition because, suppose if currently we are at (1,2) and interchange with (2,1).
    # ! Then later we will come to (2,1) and interchange with (1,2), resulting in no net change.
    # ! We avoid this by interchanging only once by imposing condition i<=j
    
    # ? Finding transpose
    for i in range(m):
        for j in range(n):
            if i <= j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # # ? Reversing each row
    for i in range(m):
        matrix[i].reverse()

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
