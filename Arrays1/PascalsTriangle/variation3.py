
# TODO: Given the number of rows n. Print the first n rows of Pascal’s triangle.

def nCr(n, r):
    val = 1
    
    for i in range(r):
        val = val * (n - i)
        val = val / (i + 1)
        # val = val * ((n - i)/(i + 1))
    return int(val)

# Naive solution
def pascalsTriangleNaive(n):
    # triangle = []

    for row in range(1, n + 1):
        # thisRow = []
        for col in range(1, row + 1):
            N = row - 1
            r = col - 1
            print(nCr(N, r), end=" ")
            # thisRow.append(nCr(N, r))
        print()
        # triangle.append(thisRow)
    print("........")
    # return triangle

# ? Time Complexity of Naive Solution : O(n*n*r) ~ O(n^3), where n = number of rows, and r = column index.
# ? Reason: The row loop will run for approximately n times. And generating a row using the naive approach of variation 2 takes O(n*r) time complexity.
# ? Space Complexity of Naive Solution : O(1) as we are not using any additional space
# ! Note that the Naive approach is the combination of variation 1 and naive approach in variation 2

# Optimal solution
def generateRow(n):
    currentElement = 1
    elements = [currentElement]
    # print(currentElement, end = " ")
    for i in range(1, n):
        currentElement = currentElement * (n - i)
        currentElement = int(currentElement / (i))  # currentElement // i
        elements.append(currentElement)
        # print(currentElement,end=" ")
    return elements

def pascalsTriangleOptimal(n):
    triangle = []
    for row in range(1, n + 1):
        currentRow = generateRow(row)
        triangle.append(currentRow)
    return triangle


#Main
triangle = pascalsTriangleOptimal(5)
for row in triangle:
    for ele in row:
        print(ele, end=" ")
    print()

# ? Time Complexity: O(n^2), where n = number of rows(given).
# ? Reason: We are generating a row for each single row. The number of rows is n. And generating an entire row takes O(n) time complexity.

# ? Space Complexity: In this case, we are only using space to store the answer. That is why space complexity can still be considered as O(1).