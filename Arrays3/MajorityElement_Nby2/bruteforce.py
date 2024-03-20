'''
Problem Statement: Given an array of N integers, 
write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.
'''

def majorityEle_Nby2(array):
    n = len(array)

    for i in range(n):
        ele = array[i]
        cnt = 0
        for j in range(n):
            if array[j] == ele:
                cnt += 1
        
        if cnt > (n // 2):
            return array[i]
    
    return -1

# Main
array = [2,2,1,1,1,2,2]
array1 = [4,4,2,4,3,4,4,3,2,4]
print(array, "\nMajority Element: ", majorityEle_Nby2(array))
print(array1, "\nMajority Element: ", majorityEle_Nby2(array1))

# ? Time Complexity : O(N^2) as we are using two nested loops.
# ? Space Complexity : O(1) as we are not using any additional space.