'''
Problem Statement: Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).
'''

def pow(x, n):
    isNegative = False
    ans = 1.0
    if n < 0:
        isNegative = True
        n = n * (-1)
    for i in range(n):
        ans = ans * x
    if isNegative:
        ans = 1 / ans
    return ans

# Main
print(pow(2, 10))
print(pow(2, -3))

# ? Time Complexity: O(N) as we are using 1 for loop.
# ? Space Complexity: O(1) as we are not using any additional space.