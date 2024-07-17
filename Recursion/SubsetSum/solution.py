'''
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.
'''

class Solution:
    def __init__(self):
        self.subsetSums = []
    
    def subsetSum(self, ind, sum, n, arr):
        if ind == n:
            self.subsetSums.append(sum)
            return
        self.subsetSum(ind + 1, sum + arr[ind], n, arr)
        self.subsetSum(ind + 1, sum, n, arr)

    def findAllSubsetSums(self, arr):
        n = len(arr)
        self.subsetSum(0, 0, n, arr)   # ! Index 0  is starting index and index 1 is starting sum

        self.subsetSums.sort()
        return self.subsetSums

# Main
arr = [3, 1, 2]
print(Solution().findAllSubsetSums(arr))

# ? Time Complexity: O(2^N) + O(2^Nlog(2^N)) as for each of the N elements in the array, we can either choose to include / exclude it in our subset and we also have to sort the subsets sum.
# ? Space Complexity: O(2^N) + O(log2N) as we are storing the sums of all subsets as for array of N elements, there are 2^N subsets. 
# ?                   But since we use recursion, we can consider auxillary stack space of O(N) as we can have a maximum N elements in the recursive stack space.