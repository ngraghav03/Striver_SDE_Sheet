'''
Problem Statement: Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.
'''

# ! This Solution passes the reference to the updated ds for all recursive calls, but appends a copy of it for the answer.

class Solution:
    def __init__(self):
        self.ans = []

    def findSubsets(self, ind, ds, n, arr):
        print(ind, ds, self.ans)
        self.ans.append(list(ds))
        
        for i in range(ind, n):
            if i != ind and arr[i] == arr[i - 1]:
                continue
            ds.append(arr[i])
            self.findSubsets(i + 1, ds, n, arr)
            ds.pop()


    def subsetsWithDuplicate(self, arr):
        ds = []
        n = len(arr)

        arr.sort()
        self.findSubsets(0, ds, n, arr)
        return self.ans

# ----------------------------------------------------------------------------------------------------
# ! This Solution is done with popping part of the backtracking process. This uses a self.combination array for all recursive calls. - takes less space 

class Solution:
    def __init__(self):
        self.ans = []
        self.subSet = []

    def findSubsets(self, ind, n, arr):
        # print(ind, self.subSet, self.ans)
        self.ans.append(list(self.subSet))
        
        for i in range(ind, n):
            if i != ind and arr[i] == arr[i - 1]:
                continue
            self.subSet.append(arr[i])
            self.findSubsets(i + 1, n, arr)
            self.subSet.pop()


    def subsetsWithDuplicate(self, arr):
        n = len(arr)

        arr.sort()
        self.findSubsets(0, n, arr)
        return self.ans
# Main
arr = [1, 2, 2]
print(Solution().subsetsWithDuplicate(arr))

# ? Time Complexity: O(2^N) for generating every subset and O(k) to insert every subset into ds where k is average length of every subset. Or we can consider atmost O(N) time for it.
# ?                  So overall TC is O(N * 2^N)

# ? Space Complexity: O(2^N) * O(k) as we store all the subsets and k is the average length of subsets.