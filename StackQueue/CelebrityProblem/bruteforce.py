'''
Problem Statement:
A celebrity is someone who is known to everyone but does not know anyone. So, if you are a celebrity at a party, you will be known to everyone, but you won’t know anyone there.
This situation is represented in the form of an N x N binary matrix. So, every cell can either have a value of 0 or 1. If matrix[i][j] = 1, this means that the ith person knows the jth person.
You have to tell whether a celebrity is present at the party or not. If it is present, we also have to tell which element (person) is the celebrity.
'''

def findCelebrity(matrix):
    n = len(matrix)
    Iknow = [0] * n
    knowMe = [0] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                Iknow[i] += 1
                knowMe[j] += 1
    
    for i in range(n):
        if Iknow[i] == 0 and knowMe[i] == n - 1:
            return i
    
    return -1

# Main
matrix = [[0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(findCelebrity(matrix))

# ? Time Complexity: O(N^2) + O(N)
# ? Space Complexity: O(2N)