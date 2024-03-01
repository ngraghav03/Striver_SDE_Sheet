'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1 '''

# ! In the better solution, we already had a time complexity of about O(n^2). Since we have a 2D array, that is acceptable (as we cant reduce the TC even further),
# ! But we can reduce the space complexity

# TODO: To eliminate the row and col arrays, we need to do everything inside the matrix itself.

def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        print("m = ", m, "and n = ",n)
        '''rows = [0] * m
        cols = [0] * n'''

        # indicates that the 1st column doesn't have 0 (initially)
        col0 = 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0

        print(matrix)

        #Processing (1,1) to (m-1,n-1)
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    if matrix[i][j] != 0:
                        matrix[i][j] = 0
        print("After adding zeroes row wise : \n", matrix,"\n")

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    if matrix[i][j] != 0:
                        matrix[i][j] = 0
        print("After adding zeroes col wise: \n", matrix,"\n")

        #Better way to process (1,1) to (m-1,n-1)
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if (matrix[i][j] != 0):
        #             if(matrix[i][0] == 0 or matrix[0][j] == 0):
        #                 matrix[i][j] = 0

        if matrix[0][0] == 0:
            matrix[0] = [0] * n
        print("After 1st row checking to matrix\n", matrix)

        if col0 == 0:
            for i in range(m):
                matrix[i][0] = 0
        print("After applying col0 to matrix\n", matrix)

        

#Main
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix3 = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
matrix4 = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
# ? solution_instance = Solution()
# ? solution_instance.setZeroes(matrix1)
# solution_instance.setZeroes(matrix2)
setZeroes(matrix4)
# Now, the 'matrix' variable is modified in-place with the zero-set values.
print("Final answer: ", matrix4)
# print(matrix1)


# ? Time Complexity : O[(m x n) + (m x n) + (m x n) + (m + n)] ~ O(n^2) -> Good Solution
# ?  with better way: O[(m x n) + (m x n)           + (m + n)] ~ O(n^2) -> Good Solution

# ? Space Complexity : O(1) as we are not using any additional space
