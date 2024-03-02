
# TODO: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

# ? The element at row r and col c is (r-1)C(c-1).
# ? Eg: The element at r=3, c=2 is 2C1 = 2 i.e., (3-1)C(2-1).

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    print("Element at r = ",r, " c = ",c," is ", int(element))

def nCr(n, r):
    val = 1
    
    for i in range(r):
        val = val * (n - i)
        val = val / (i + 1)
        # val = val * ((n - i)/(i + 1))
    return val

#Main
pascalTriangle(3,2)
# ? Time Complexity: O(c), where c = given column number.
# ? Reason: We are running a loop for r times, where r is c-1.

# ? Space Complexity: O(1) as we are not using any extra space.