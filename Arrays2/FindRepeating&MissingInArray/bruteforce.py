'''
Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. 
The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
'''

# ! We traverse through the array and find the number of occurences of each element, and find which of them is 2 and 0

def findRepeating_MissingNumbers(array):
    n = len(array)

    repeating = -1
    missing = -1

    for i in range(1, n + 1):

        count = array.count(i)
        # count = 0
        # for j in range(n):
        #     if(array[j] == i):
        #         count += 1

        if count == 0:
            missing = i
        elif count == 2:
            repeating = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

# Main
array = [3,1,2,5,3]
repeating, missing = findRepeating_MissingNumbers(array)
print("Repeating: ", repeating)
print("Missing: ", missing)

# ? Time Complexity: O(N^2) as we are using two nested loops 
# ? -> for each element we are calculating the number of occurences which is atmost N*N operations.

# ? Space Complexity: O(1), because we are storing the frequencies of N elements.