'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# ! When the elements of the array are unique, then all the subsets got are unique, as there cannot be any repetitions in the subsets.
# ! Eg : Subsets (1, 2) and (2, 1) cannot be formed if the array was unique.

class Solution:
    def __init__(self):
        self.subSets = []

    def findSubsets(self, arr, n, ind, subset):
        if ind == n:
            self.subSets.append(subset)
            return
        self.findSubsets(arr, n, ind + 1, subset + [arr[ind]])
        self.findSubsets(arr, n, ind + 1, subset)

    def findAllSubsets(self, arr):
        n = len(arr)

        self.findSubsets(arr, n, 0, [])

        return self.subSets
    
# Main
arr = [3, 1, 2]
print(Solution().findAllSubsets(arr))