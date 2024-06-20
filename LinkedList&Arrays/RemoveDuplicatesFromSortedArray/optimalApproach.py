'''
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.
'''

def removeDuplicates(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        
    return i + 1

# Main
A = [0,0,1,1,1,2,2,3,3,4]
B = [1,1,2]
print(A, "-> ", removeDuplicates(A))
print(B, "-> ", removeDuplicates(B))

# ? Time Complexity: O(N) 
# ? Space Complexity Complexity: O(1) 