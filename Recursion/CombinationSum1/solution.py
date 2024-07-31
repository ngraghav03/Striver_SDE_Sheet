'''
Problem Statement: 
Given an array of distinct integers and a target, you have to return the list of all unique combinations where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from the given array an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
# ! This Solution is done without popping part of the backtracking process. This creates a fresh copy of combination for every node of the recursion tree - takes more space.
class Solution:
    def __init__(self):
        self.combinations = []

    def findCombinations(self, ind, target, combination, arr, n):
        # print(ind, target, combination)
        if ind == n:
            if target == 0:
                self.combinations.append(combination)
            return

        if arr[ind] <= target:
            self.findCombinations(ind, target - arr[ind], combination + [arr[ind]], arr, n)
        self.findCombinations(ind + 1, target, combination, arr, n)


    def combinationSum(self, arr, target):
        n = len(arr)
        self.findCombinations(0, target, [], arr, n)

        return self.combinations

# ----------------------------------------------------------------------------------------------------
# ! This Solution is done with popping part of the backtracking process. This uses a self.combination array for all recursive calls. - takes less space 

class Solution:
    def __init__(self):
        self.combinations = []
        self.combination = []

    def findCombinations(self, ind, target, arr, n):
        print(ind, target, self.combination, self.combinations)
        
        if target == 0:
            # print("Appending ", self.combination)
            self.combinations.append(self.combination.copy())
            # print("After appending ", self.combinations)
            return

        if ind == n:
            return

        if arr[ind] <= target:
            self.combination.append(arr[ind])
            self.findCombinations(ind, target - arr[ind], arr, n)
            self.combination.pop()

            self.findCombinations(ind + 1, target, arr, n)
        
        else:
            return


    def combinationSum(self, arr, target):
        n = len(arr)
        self.findCombinations(0, target, arr, n)

        return self.combinations

# Main
arr = [2, 3, 6, 7]
target = 7

# arr1 = [1, 2]
# target1 = 3

print(Solution().combinationSum(arr, target))
# print(Solution().combinationSum(arr1, target1))