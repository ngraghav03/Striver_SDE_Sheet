'''
Problem Statement: Given an array of N integers, 
write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.
'''

def majorityEle_Nby2(array):
    n = len(array)

    current = -1
    count = 0
    ptr = 0

    while ptr < n:
        if count == 0:
            count = 1
            current = array[ptr]
        
        elif current == array[ptr]:
            count += 1
        
        else:
            count -= 1
        ptr += 1

    # We need to check if the current element is the majority element in case we are not sure if majority element exists or not.
    # If question guarantees the existence of a majority element, then we can just return it.
    cnt = 0
    for i in range(n):
        if array[i] == current:
            cnt += 1
    
    if cnt > (n // 2):
        return current
    else:
        return -1

# Main
array = [2,2,1,1,1,2,2]
array1 = [4,4,2,4,3,4,4,3,2,4]
print(array, "\nMajority Element: ", majorityEle_Nby2(array))
print(array1, "\nMajority Element: ", majorityEle_Nby2(array1))

# ? Time Complexity : O(N^2) as we are using two nested loops.
# ? Space Complexity : O(1) as we are not using any additional space.