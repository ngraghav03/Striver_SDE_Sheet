'''
Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. 
Assuming there is only one duplicate number, your task is to find the duplicate number.
'''
# TODO: We note the frequency of each element in the array and check which element we are encountering already has frequency 1


def findDuplicateNumber(array):

    n = len(array)

    frequencies = [0] * (n + 1)

    for i in range(1, n):
        if frequencies[array[i]] == 0:
            frequencies[array[i]] = 1
        else:
            return array[i]
    return -1   

# Main
array = [1, 3, 4, 2, 2]
print("Array = ", array)
duplicateEle = findDuplicateNumber(array)
print("Duplicate number: ", duplicateEle)

# ? Time Complexity: O(N). To calculate the frequencies.
# ? Space Complexity: O(N), as we are storing the frequencies of N elements