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

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1

        for i in range(m):
            if rows[i] == 1:
                matrix[i] = [0] * n

        for j in range(n):
            if cols[j] == 1:
                for i in range(m):
                    matrix[i][j] = 0

        # Better way to get the final matrix 
        ''' for i in range(n):
        # for j in range(m):
        #     if row[i] or col[j]:
                 matrix[i][j] = 0 '''
        
#Main
matrix = eval(input())
solution_instance = Solution()
solution_instance.setZeroes(matrix)

# Now, the 'matrix' variable is modified in-place with the zero-set values.
print(matrix)

# ? Time Complexity : O[(m x n) + (m x n) + (m x n)] ~ O(n^2) -> Good Solution
# ?  with better way: O[2(m x n)] ~ O(n^2) -> Good Solution
# ? Space Complexity : O(m + n) as we are  using two arrays rows and cols to store if a row/column has 0 in it or not.
# ! The interviewer will not be happy with the space complexity, so he will ask you to optimize.