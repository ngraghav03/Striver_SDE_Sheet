'''
Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. 
If no such element exists, return an empty vector.
'''

def majorityEle_Nby3(array):
    majorityElements = []
    n = len(array)
    d = {}
    
    for i in range(n):
        if array[i] in d:
            d[array[i]] += 1
        else:
            d[array[i]] = 1

    for num, count in list(d.items()):
        if count > (n // 3):
            majorityElements.append(num)
        
        if len(majorityElements) == 2:
            break 
    
    return majorityElements

# Main
arr = [11, 33, 33, 11, 33, 11]
print(majorityEle_Nby3(arr))

# ? Time Complexity: O(2N) : O(N) for preparing the dictionary and O(N) for finding the majority elements from the dictionary
# ? Space Complexity: O(N) as we will store atmost N items in the dictionary