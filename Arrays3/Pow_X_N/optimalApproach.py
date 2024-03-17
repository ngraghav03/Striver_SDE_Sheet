'''
Problem Statement: Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).
'''

'''
Example:
2^10 = (2x2)^(10/2) = 4^5 
4^5 = 4 x 4^4
4^4 = (4x4)^(4/2) = 16^2
16^2 = (16x16)^(2/2) = 256^1
256^1 = 256 * 256^0

Hence ans = 256 x 4 = 1024
'''

def pow(x, n):
    isNegative = False
    ans = 1.0
    if n < 0:
        isNegative = True
        n = n * (-1)
    
    # ! Binary Exponentiation
    nn = n
    ans = 1.0

    while nn > 0:
        if nn % 2 == 0:     # If power is even
            x = x * x       # 2^10 = (2x2)^(10/2) = 4^5
            nn = nn // 2
        else:               # If power is odd
            ans = ans * x   # 4^5 = 4 x 4^4
            nn = nn - 1

    if isNegative:
        ans = 1 / ans
    return ans

# Main
print(pow(2, 10))
print(pow(2, -3))

# ? Time Complexity: O(log2 N) as we are using dividing the power we need to compute by half in each iteration.
# ?                  Mostly any program that uses binary algorithm / divide the solution by half has O(log2 N) time complexity.
# ? Space Complexity: O(1) as we are not using any additional space.