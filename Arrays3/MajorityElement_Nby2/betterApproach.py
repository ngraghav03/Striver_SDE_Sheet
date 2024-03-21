'''
Problem Statement: Given an array of N integers, 
write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.
'''

def majorityEle_Nby2(array):
    n = len(array)
    counter = {}
    for i in range(n):
        if array[i] in counter:
            counter[array[i]] += 1
        else:
            counter[array[i]] = 1
    
    for num, count in list(counter.items()):
        if count > (n // 2):
            return num
    
    return -1

# Main
array = [2,2,1,1,1,2,2]
array1 = [4,4,2,4,3,4,4,3,2,4]
print(array, "\nMajority Element: ", majorityEle_Nby2(array))
print(array1, "\nMajority Element: ", majorityEle_Nby2(array1))

# ? Time Complexity : O(2N), where O(N) is to create the hashmap / dictionary and O(N) to find the majority element from the dictionary
# ? Space Complexity : O(N) as we are storing at most N elements in the dictionary