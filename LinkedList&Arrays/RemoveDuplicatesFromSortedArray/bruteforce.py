'''
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.
'''

def removeDuplicates(nums):
    n = len(nums)
    hashSet = set()
    for i in range(n):
        hashSet.add(nums[i])
    j = 0
    for x in hashSet:
        nums[j] = x
        j += 1
    return len(hashSet)

# Main
A = [0,0,1,1,1,2,2,3,3,4]
B = [1,1,2]
print(A, "-> ", removeDuplicates(A))
print(B, "-> ", removeDuplicates(B))

# ? Time Complexity: O(NlogN) + O(N). O(NlogN) is for adding N elements to the hashSet, each of which takes O(logN) time at the maximum.
# ?                  The second for loop runs for a maximum of N times, if there are N unique elements in the array/hashSet.
# ? Space Complexity Complexity: O(N) as we store a maximum of N elements in the hashSet. 