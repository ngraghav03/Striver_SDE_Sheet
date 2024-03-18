'''
Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the
constraints that from each cell you can either only move to the rightward direction or the downward direction.
'''
# ! We are taking exactly m + n - 2 steps to reach the end.
# ! We are taking (m - 1) downward steps and (n - 1) rightward steps
# ! Since we need an m+n-2 number of steps to reach the end among those steps if we choose n-1 rightward direction 
# ! or m-1 downward direction and calculate the combinations ( i.e: (m+n-2)C(n-1) or (m+n-2)C(m-1) we’ll get the total number of paths.

def gridUniquePaths_combinatorics(m, n):
    N = n + m - 2
    r = m - 1       # r =  min(m, n) - 1
    res = 1
    for i in range(1, r + 1):
        res = res * (N - r + i) / i
    return int(res)

# Main
m = 2
n = 2
uniquePaths = gridUniquePaths_combinatorics(3, 7)
print("Number of unique paths for m = ", m, "and n = ", n, " = ",uniquePaths)


# ? Time Complexity: O(m -1) or O(n - 1) i.e., O(m) or O(n). 
# ?                  We can choose ensure minimum time complexity, by calculating min(m, n). So C is O(min(m, n))

# ? Space Complexity: O(1) as we are not using any additional space