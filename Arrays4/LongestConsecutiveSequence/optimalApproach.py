'''
Problem Statement: You are given an array of 'N' integers. 
You need to find the length of the longest sequence which contains the consecutive elements.
'''

def longestConsecutiveSequence(array):
    n = len(array)
    # longest is initialized to 1 as any element is a consecutive sequence in itself.
    longest = 1

    # Instead of calculating length of consecutive sequences for all elements,
    # We only do so for starting elements.
    # X is a starting element in the array if X - 1 is not there in the array.

    # For eg: Let 100, 101 and 102 be in the array.
    # We calculate the length of consecutive sequence starting from 100 alone, 
    # as well as the length of consecutive sequence starting from 101 is 1 + that of 100.
    # f(101) = 1 + f(100)

    # We will use a set to store the distinct/unique elements to make sure we don't do duplicate computations.
    st = set(array)

    for X in st:
        if (X - 1) in st:
            continue
        else:
            next = X + 1
            length = 1
            while next in st:
                next += 1
                length += 1
            
            longest = max(longest, length)
            

    return longest

# Main
arr = [100, 200, 1, 3, 2, 4]
arr1 = [3, 8, 5, 7, 6]
arr2 = [1,3,5,7]
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr))
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr1))
print("Length of longest consecutive sequence: ", longestConsecutiveSequence(arr2))

# ? Time Complexity: O(N) + O(2N) ~ O(3N), O(N) for adding elements to the set,
# ? another O(N) for selecting elements to check if it is starting ele or not (for loop)
# ? The third O(N) is from while loop which runs for atmost N iterations for all N elements together.

# ? Space Complexity: O(N) as we are using a set that can have atmost N elements (if all are unique).