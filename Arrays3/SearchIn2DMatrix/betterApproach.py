'''
Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number of rows and columns, respectively. 
The elements of each row are sorted in non-decreasing order. 
Moreover, the first element of a row is greater than the last element of the previous row (if it exists). 
You are given an integer 'target', and your task is to find if it exists in the given 'mat' or not.
'''

# ? Traverse the matrix row by row to find the what row the target might be in using linear search.
# ? Once we find which row it might be in, we use binary search to find if the target is present in the row or not.
# ? To find which row the target might be in, use condition:
# ?     if matrix[row][0] <= target <= matrix[row][m - 1]

def searchIn_2DMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    row = -1
    for i in range(n):
        if matrix[i][0] <= target and target <= matrix[i][m - 1]:
            row = i
            break
    
    low = 0
    high = m - 1
    while low <= high:
        mid = (low + high) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
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

# ? Time Complexity: O(N + logM).
# ?                  We use atmost O(N) for finding thr row the target might be in and O(logM) to do binary search on that row
# ? Space Complexity: O(1) as we are not using any additional space 