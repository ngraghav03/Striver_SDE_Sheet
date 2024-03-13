'''
Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. 
The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
'''

def findRepeating_MissingNumbersXOR(array):
    repeating, missing = -1, -1

    n = len(array)
    num = 0
    # XORing (array) and [1, N]
    for i in range(n):
        num = num ^ array[i] ^ (i + 1)
    print("XOR Of array and [1,N] = ", num)

    # Finding the rightmost differentiating bit.
    bitNo = 0
    numcopy = num
    while(numcopy % 2 != 1):
        numcopy = numcopy >> 1
        bitNo += 1
    print("Differentiating bit :", bitNo)

    Club0 = []
    Club1 = []
    club0 = 0
    club1 = 0
    # Classifying array elements and numbers from [1, N] based on differentiating bit
    # When we find the club in which a number falls, we directly XOR it with the corresponding club
    # Then at the end, both the clubs will fetch the missing and repeating numbers together
    # For clarity sake, I have stored the classfied numbers in an array
    for i in range(n):
        # Classifying array elements
        if(array[i] >> bitNo == 0):
            Club0.append(array[i])
            club0 = club0 ^ array[i]
        else:
            Club1.append(array[i])
            club1 = club1 ^ array[i]
        
        # Classifying numbers from [1, N]
        if((i + 1) >> bitNo == 0):
            Club0.append((i + 1))
            club0 = club0 ^ (i + 1)
        else:
            Club1.append((i + 1))
            club1 = club1 ^ (i + 1)

    print("Club0 = ", Club0, "\nClub1 = ", Club1)
    print("XOR of Club0 = ", club0, "\nXOR of Club1 = ", club1)
    # We now know the repeating and missing numbers, but we don't know which is which.

    for i in range(n):
        if array[i] == club0:
            # This means that the club0 is present in the array, which means that is the repeating number and the other is the missing number
            repeating = club0
            missing = club1
            break
        elif array[i] == club1:
            # This means that the club1 is present in the array, which means that is the repeating number and the other is the missing number
            repeating = club1
            missing = club0

    return [repeating, missing]
    


# Main
array = [3,1,2,5,3]
array1 = [4, 3, 6, 2, 1, 1]
repeating, missing = findRepeating_MissingNumbersXOR(array1)
print("Repeating: ", repeating)
print("Missing: ", missing)

# ? Time Complexity: O(4*N) ~ O(N) because we are running several loops which run for at most N times.
# ?                  Some loops can be clubbed or separated but by approximation it is O(N).
# ? Space Complexity: O(N) as we are not using any extra space, 
# ?                   but we use O(2*N) to store the classified elements for clarity sake (not part of original solution)