
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

def mergeOverlappingSubIntervals(intervals):
    mergedIntervals = []
    n = len(intervals)
    
    intervals.sort(key=lambda x: x[0])

    # startInterval = intervals[0][0]
    # endInterval = intervals[0][1]

    # This currentInterval list stores the start and end intervals of the current joint interval
    currentInterval = intervals[0]

    # Eg: intervals = [[1,3],[2,6]] 

    for i in range(1, n):
        print(intervals[i])
        print("Current Interval",currentInterval)
        
        # If the starting of the current interval is between the start and end intervals variables, then we update the current interval accordingly
        if intervals[i][0] >= currentInterval[0] and intervals[i][0] <= currentInterval[1]:
            currentInterval[0] = min(currentInterval[0], intervals[i][0])
            # start -> min(1, 2)
            currentInterval[1] = max(currentInterval[1], intervals[i][1])

            if i == n - 1:
                mergedIntervals.append(currentInterval)

        elif intervals[i][0] > currentInterval[1]:
            mergedIntervals.append(currentInterval)

        # Update the current start and end interval
            currentInterval = [intervals[i][0],intervals[i][1]]
            if i == n - 1:
                mergedIntervals.append(intervals[i])

        print("#",currentInterval)
        print("Merged Interval: ",mergedIntervals)

# Main
intervals = [[2,3],[1,2],[4,6],[7,9],[8,10]]
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
mergeOverlappingSubIntervals(intervals)

# ? Time Complexity: O(N*logN) + O(N), where N = the size of the given array.
# ? Reason: Sorting the given array takes  O(N*logN) time complexity. Now, after that, we are just using a single loop that runs for N times. So, the time complexity will be O(N).

# ? Space Complexity: O(N), as we are using an answer list to store the merged intervals. Except for the answer array, we are not using any extra space.