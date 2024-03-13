'''
Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. 
The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.
'''
# ! We find the frequency of each element and find which has freq 2 (repeating) and 0 (missing) 

def findRepeating_MissingNumbers(array):
    n = len(array)
    frequencies = [0] * (n + 1)
    
    # i is the index of the array. We are updating the freq array for element array[i] 
    for i in range(n):  # i is the index of the array,element from [1,N]
        frequencies[array[i]] += 1  #freq[array[i]]

    missing = -1
    repeating = -1

    for i in range(n + 1):
        if frequencies[i] == 0:
            missing = i
        elif frequencies[i] == 2:
            repeating = i
    
    return [repeating, missing]


# Main
array = [3,1,2,5,3]
repeating, missing = findRepeating_MissingNumbers(array)
print("Repeating: ", repeating)
print("Missing: ", missing)

# ? Time Complexity: O(N) + O(N) ~ O(2N). The first O(N) is to find the frequency of elements. 
# ? The second O(N) is to find which is the repeating and the missing number

# ? Space Complexity: O(N), because we are storing the frequencies of N elements.