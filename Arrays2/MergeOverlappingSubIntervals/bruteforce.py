'''
Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.  
Example 1: 
Input: intervals=[[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
intervals.

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].
'''

def mergeOverlappingSubIntervals(arr):
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n): # select an interval:
        start, end = arr[i][0], arr[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        # check the rest of the intervals:
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans

# Main
intervals = [[2,3],[1,2],[4,6],[7,9],[8,10]]
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
print(mergeOverlappingSubIntervals(intervals))

# ? Time Complexity: O(N*logN) + O(2*N), where N = the size of the given array.
# ? Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are using 2 loops i and j. But while using loop i, 
# ? we skip all the intervals that are merged with loop j. So, we can conclude that every interval is roughly visited twice(roughly, once for checking or skipping and once for merging). 
# ? So, the time complexity will be 2*N instead of N^2.

# ? Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.