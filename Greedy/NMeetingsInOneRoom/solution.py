'''
Problem Statement: There is one meeting room in a firm. You are given two arrays, start and end each of size N.For an index "i", 
start[i] denotes the starting time of the ith meeting while end[i]  will denote the ending time of the ith meeting. 
Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a  particular time. 
Print the order in which these meetings will be performed.
'''

# ^ Say if you have two meetings, one which gets over early and another which gets over late. Which one should we choose? 
# ^ If our meeting lasts longer the room stays occupied and we lose our time. 
# ^ On the other hand, if we choose a meeting that finishes early we can accommodate more meetings. 
# ^ Hence we should choose meetings that end early and utilize the remaining time for more meetings.

class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

def maxMeetings(startArray, endArray, n):
    meet = [Meeting(startArray[i], endArray[i], i + 1) for i in range(n)]
    sorted(meet, key=lambda x: (x.end, x.pos))
    # * We are sorting the meeting objects by its end, and then pos (if two meetings end are same)
    answer = [meet[0].pos]
    limit = meet[0].end

    for i in range(1, n):
        if meet[i].start >= limit:
            answer.append(meet[i].pos)
            limit = meet[i].end
    
    return answer

# Main
start = [1,3,0,5,8,5]
end = [2,4,5,7,9,9]
print("Order: ")
print(maxMeetings(start, end, len(start)))

# ? Time Complexity : O(N) + O(NlogN) + O(N) ~ O(NlogN)
# ?                   O(N) for creating N different objects, O(NlogN) for sorting the array of objects based on end and then pos, 
# ?                   then O(N) for finding which meetings can be held (one for loop)
# ? Space Complexity : O(N) as we create N different objects. More precisely, it is O(3N).