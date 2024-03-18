'''
Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the
constraints that from each cell you can either only move to the rightward direction or the downward direction.
'''
4
def gridUniquePaths_dp(m, n):
    count = 0
    i = 0 
    j = 0
    dp = [[-1 for i in range(n)] for j in range(m)] 

    count += gridUniquePaths(i, j, m, n, dp)
    return count

def gridUniquePaths(i, j, m, n, dp):
    
    print("(",i,",",j,")")
    if i >= m or j >= n:
        return 0
    if i == (m - 1) and j == (n - 1):
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = gridUniquePaths(i + 1, j, m, n, dp) + gridUniquePaths(i, j + 1, m, n, dp)
        return dp[i][j]
    


# Main
m = 2
n = 2
uniquePaths = gridUniquePaths_dp(3, 7)
print("Number of unique paths for m = ", m, "and n = ", n, " = ",uniquePaths)


# ? Time Complexity: The time complexity of this recursive solution is exponential.
# ? Space Complexity: As we are using stack space for recursion so the space complexity will also be exponential.
