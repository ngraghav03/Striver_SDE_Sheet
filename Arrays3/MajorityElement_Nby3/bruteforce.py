'''
Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. 
If no such element exists, return an empty vector.
'''

def majorityEle_Nby3(array):
    majorityElements = []
    n = len(array)

    for i in range(n):

        if len(majorityElements) == 0 or majorityElements[0] != array[i]:
            ele = array[i]
            cnt = 0
            for j in range(n):
                if array[j] == ele:
                    cnt += 1
            
            if cnt > (n // 3):
                majorityElements.append(ele)
        
        if len(majorityElements) == 2:
            break
    
    return majorityElements

# Main
arr = [11, 33, 33, 11, 33, 11]
print(majorityEle_Nby3(arr))

# ? Time Complexity: O(N^2) as we use two nested loops
# ? Space Complexity: O(1) as we are not using any additional space