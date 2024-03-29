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

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1
                    for l in range(n):
                        if matrix[i][l] != 0:
                            matrix[i][l] = -1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

#Main
matrix = eval(input())
solution_instance = Solution()
solution_instance.setZeroes(matrix)

# Now, the 'matrix' variable is modified in-place with the zero-set values.
print(matrix)

# ? Time Complexity : O[(m x n) * (m + n) + (m x n)] ~ O(n^3) -> Bad Idea
# ? Space Complexity : O(1) as we are not using any additional space
 