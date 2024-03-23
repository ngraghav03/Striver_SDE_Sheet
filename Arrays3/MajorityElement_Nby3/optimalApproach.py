'''
Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. 
If no such element exists, return an empty vector.
'''

def majorityEle_Nby3(array):
    majorityElements = []

    N = len(array)
    ptr = 0
    current1, current2 = -1, -1
    count1, count2 = 0, 0

    while ptr < N:
        # The element should not be equal to current2 if we want to reassign current1
        if count1 == 0 and array[ptr] != current2 :
            current1 = array[ptr]
            count1 += 1

        # The element should not be equal to current1 if we want to reassign current2
        elif count2 == 0 and array[ptr] != current1:
            current2 = array[ptr]
            count2 += 1
        
        elif array[ptr] == current1:
            count1 += 1

        elif array[ptr] == current2:
            count2 += 1 
        
        else:
            count1 -= 1
            count2 -= 1

        ptr += 1

    # Manually check if the current1 and current2 elements are majority elements
    cnt1 = 0
    cnt2 = 0

    '''
    It is possible that this way of checking can take less time as we break out of loop immediately 
    if it is a majority element and not calculating its count thereafter.

    for i in range(N):
        if array[i] == current1:
            cnt1 += 1
            if cnt1 > (N // 3):
                majorityElements.append(current1)
                break

    for i in range(N):
        if array[i] == current2:
            cnt2 += 1
            if cnt2 > (N // 3):
                majorityElements.append(current2)
                break'''

    for i in range(N):
        if array[i] == current1:
            cnt1 += 1
        elif array[i] == current2:
            cnt2 += 1
    
    if cnt1 > (N // 3):
        majorityElements.append(current1)
    if cnt2 > (N // 3):
        majorityElements.append(current2)
    
    return majorityElements

# Main
arr = [11, 33, 33, 11, 33, 11]
print(majorityEle_Nby3(arr))

# ? Time Complexity: O(2N) : O(N) for preparing the dictionary and O(N) for finding the majority elements from the dictionary
# ? Space Complexity: O(N) as we will store atmost N items in the dictionary