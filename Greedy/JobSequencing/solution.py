'''
Problem Statement: You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. 
Find the number of jobs done and the maximum profit that can be obtained. Each job takes a single unit of time and only one job can be performed at a time.

# ^ Examples:
Example 1:

Input: N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

Output: 2 60

Explanation: The 3rd job with a deadline 1 is performed during the first unit of time .The 1st job is performed during the second unit of time as its deadline is 4.
Profit = 40 + 20 = 60

Example 2:

Input: N = 5, Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}

Output: 2 127

Explanation: The  first and third job both having a deadline 2 give the highest profit. 
Profit = 100 + 27 = 127
'''

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

# ! Approach:  The strategy to maximize profit should be to pick up jobs that offer higher profits. Hence we should sort the jobs in descending order of profit. 
# !Now say if a job has a deadline of 4 we can perform it anytime between day 1-4, 
# ! but it is preferable to perform the job on its last day. This leaves enough empty slots on the previous days to perform other jobs.

def jobSequencing(jobs):
    
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    maxDeadline = jobs[0].deadline
    for i in range(1, len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i].deadline)
    # Create an answer array with length = max deadline
    answer = [-1] * (maxDeadline + 1)

    jobsDone = 0
    jobsProfit = 0
    timePassed = 0

    for i in range(len(jobs)):
        # print(jobs[i].deadline)
        for j in range(jobs[i].deadline, 0, -1):
            if answer[j] == -1:              # If slot is free, then do the job on its last day. If not, the previous and so on.
                
                answer[j] = jobs[i].id        # Update the slot
                
                jobsDone += 1                       # Increment the number of jobs done
                jobsProfit += jobs[i].profit        # Update the profit got.
                
                break
    
    return answer, jobsDone, jobsProfit

# Main
jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 2, 40), Job(4, 2, 30)]

schedule, jobsDone, jobsProfit = jobSequencing(jobs)
print("Number of jobs completed : ", jobsDone)
print("Job sequence: ", schedule)
print("Profit from jobs : ", jobsProfit)

# ? Time Complexity: O(NlogN) + O(N * M) where N is the number of jobs given and M is the maximum deadline of the jobs.
# ?                  O(NlogN) for sorting the jobs based on descending order of profit.
# ?                  O(N * M) as we are using two nested loops with one running N times and the other running maximum of M times.

# ? Space Complexity: O(M) for storing the slot-wise job sequence.