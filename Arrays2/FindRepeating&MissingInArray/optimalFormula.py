'''
Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. 
The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
'''

# ! We use Mathematical formula to find the repeating and missing numbers
# ! Sum of N numbers [1,N] 'Sn'= (N*(N+1))/2
# ! The sum with one repeating number X and missing number Y is 'S'

# ! Therefore, S - Sn = X - Y   ----> Equation 1

# ! Similarly, the sum of squares of N numbers [1,N] is 'S2n' = (N*(N+1)*(2N + 1))/6
# ! The sum of squares with one repeating number X and missing number Y is 'S2'

# ! Therefore, S2 - S2n = X^2 - Y^2   ----> Equation 2

# ! (X + Y) = (S2 - S2n)/(X - Y)    -----> Equation 3


def findRepeating_MissingNumbers(array):
    N = len(array)
    S = 0
    S2 = 0
    for i in range(N):
        S += array[i]
        S2 += array[i] * array[i]

    Sn = (N*(N + 1)) // 2
    S2n = (N*(N+1)*(2*N + 1)) // 6

    X_minus_Y = S - Sn
    X_plus_Y = (S2 - S2n) // (X_minus_Y)

    X = (X_minus_Y + X_plus_Y) // 2
    Y = X_plus_Y - X

    return [X, Y] 

    


# Main
array = [3,1,2,5,3]
repeating, missing = findRepeating_MissingNumbers(array)
print("Repeating: ", repeating)
print("Missing: ", missing)

# ? Time Complexity: O(N) as we are calculating sum of elements and squares of elements in array

# ? Space Complexity: O(1), as we are not using any additional space. 