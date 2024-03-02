
# TODO: Given the row number n. Print the n-th row of Pascal’s triangle.

def nCr(n, r):
    val = 1
    
    for i in range(r):
        val = val * (n - i)
        val = val / (i + 1)
        # val = val * ((n - i)/(i + 1))
    return int(val)

def pascalsTriangleNaive(n):
    for r in range(n):
        print(int(nCr(n - 1, r)),end = " ")
    print()

# ? Time Complexity of Naive Solution : O(n*r) ~ O(n^2)
# ? Space Complexity of Naive Solution : O(1) as we are not using any additional space

def pascalsTriangleOptimal(n):
    # elements = [1]
    currentElement = 1
    print(currentElement, end = " ")
    for i in range(1, n):
        currentElement = currentElement * (n - i)
        currentElement = int(currentElement / (i))  # currentElement // i
        # elements.append(currentElement)
        print(currentElement,end=" ")
    print()

# ? Time Complexity of Naive Solution : O(n)
# ? Space Complexity of Naive Solution : O(1) as we are not using any additional space

#Main
n = 5
pascalsTriangleOptimal(n)