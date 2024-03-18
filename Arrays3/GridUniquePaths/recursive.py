'''
Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the
constraints that from each cell you can either only move to the rightward direction or the downward direction.
'''

def gridUniquePaths_recursive(m, n):
    count = 0
    i = 0 
    j = 0
    # count += gridUniquePaths(i, j + 1, m, n, count)
    count += gridUniquePaths(i, j, m, n)
    # count += gridUniquePaths(i + 1, j,m, n, count)

    return count

def gridUniquePaths(i, j, m, n):
    
    print("(",i,",",j,")")
    if i >= m or j >= n:
        return 0
    if i == (m - 1) and j == (n - 1):
        return 1
    
    count = gridUniquePaths(i, j + 1, m, n) + gridUniquePaths(i + 1, j, m, n)
    
    return count
    


# Main
m = 2
n = 2
uniquePaths = gridUniquePaths_recursive(3, 3)
print("Number of unique paths for m = ", m, "and n = ", n, " = ",uniquePaths)


# ? Time Complexity: The time complexity of this recursive solution is exponential.
# ? Space Complexity: As we are using stack space for recursion so the space complexity will also be exponential.
