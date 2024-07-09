'''
Problem Statement: Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, 
i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change.
'''

#  TODO: Approach: We will keep a pointer at the end of the array i. Now while(V >= coins[i]) we will reduce V by coins[i] and add it to the ans array.
#  TODO: We will also ignore the coins which are greater than V and the coins which are less than V. We consider them and reduce the value of V by coins[I].

def minNoOfCoins(V):

    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

    pointer = len(denominations) - 1

    numCoins = 0


    while V > 0:
        while V >= denominations[pointer]:
            print(denominations[pointer], end = " ")
            numCoins += 1
            V -= denominations[pointer]
        
        pointer -= 1

    return numCoins

# Main
V = 87
print(minNoOfCoins(V))

# ? Time Complexity: O(V)
# ? Space Complexity: O(1)