'''
Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. 
Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
'''

'''
Example:

Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]

Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]
'''

def mergeArrays(arr1, arr2):
    
    print("arr1: ",arr1)
    print("arr2: ",arr2)
    print("********")

    n = len(arr1)
    m = len(arr2)

    ptr1 = 0
    ptr2 = 0

    mergedArray = [0 for i in range(n + m)]
    numberOfElementsAdded = 0
    # print(mergedArray)
    while ptr1 < n and ptr2 < m:
        if numberOfElementsAdded <= (n+m):
            if arr1[ptr1] <= arr2[ptr2]:
                mergedArray[numberOfElementsAdded] = arr1[ptr1]
                ptr1 += 1
                # print(mergedArray)

            elif arr1[ptr1] > arr2[ptr2]:
                mergedArray[numberOfElementsAdded] = arr2[ptr2]
                ptr2 += 1
                # print(mergedArray)
            numberOfElementsAdded += 1
    # print(mergedArray)    
    # print(".........")
    
    if ptr1 == n:
        mergedArray[numberOfElementsAdded : ] = arr2[ptr2 : ]
        ptr2 = m
    elif ptr2 == m:
        mergedArray[numberOfElementsAdded : ] = arr1[ptr1 : ]
        ptr1 = n

    arr1 = mergedArray[:n]
    arr2 = mergedArray[n:]

    print("Merged Array : ",mergedArray)
    print("arr1: ",arr1)
    print("arr2: ",arr2)
    



# Main

# arr1 = eval(input())
# arr2 = eval(input())
arr1 = [1,4,8,10]
arr2 = [2,3,9]

arr1.sort()
arr2.sort()

mergeArrays(arr1, arr2)

# ? Time Complexity: O(n + m) + O(n + m), where n and m are the sizes of the given arrays.
# ? Reason: O(n + m) is for copying the elements from arr1 and arr2 to mergedArray. And another O(n+m) is for filling back the two given arrays from mergedArray.
# ? Space Complexity: O(n + m) as we use an extra array of size m+n.