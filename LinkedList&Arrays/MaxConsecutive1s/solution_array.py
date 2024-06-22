'''
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
'''

def findMaxConsecutiveOnes(nums):
    maxCount = 0
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        
        maxCount = max(maxCount, count)
            
    return maxCount

# Main
A1 = [1,1,0,1,1,1]
A2 = [1,0,1,1,0,1]

print(A1, "-> ", findMaxConsecutiveOnes(A1))
print(A2, "-> ", findMaxConsecutiveOnes(A2))

# ? Time Complexity: O(N)
# ? Space Complexity Complexity: O(1)