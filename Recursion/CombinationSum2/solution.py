'''
Problem Statement: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. 
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''

class Solution:
    def __init__(self):
        self.combinations = set()
        self.combination = []

    def findUniqueCombinations(self, ind, target, arr, n):
        if target == 0:
            self.combinations.add(tuple(self.combination))
            return

        for i in range(ind, n):
            # ! If the array element is greater than the target, no subsequent element of the array will be <= target. So we break out of the loop.
            if arr[i] > target:
                break
            
            # ! Skip all he duplicate elements of the array and do recursive calls only for first occurence of each element.
            if i != 0 and arr[i] == arr[i - 1]:
                continue
            self.combination.append(arr[i])
            self.findUniqueCombinations(i + 1, target - arr[i], arr, n)
            self.combination.pop()
    
    def combinationSum(self, arr, target):
        n = len(arr)
        # ! We need to sort the array as we need sorted combinations
        arr.sort()
        self.findUniqueCombinations(0, target, arr, n)

        return list(self.combinations)

# Main
arr = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum(arr, target))