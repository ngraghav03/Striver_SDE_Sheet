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

'''
1.  We will declare two pointers i.e. ptr1 and ptr2. The ptr1 pointer will point to the last index of the arr1(i.e. Basically the maximum element of the array). 
    The ptr2 pointer will point to the first index of the arr2[](i.e. Basically the minimum element of the array).
2.  Now, the ptr1 pointer will move toward index 0 and the ptr2 pointer will move towards the index m-1. 
    While moving the two pointers we will face 2 different cases like the following:
        If arr1[ptr1] > arr2[ptr2]: In this case, we will swap the elements and move the pointers to the next positions.
        If arr1[ptr1] <= arr2[ptr2]: In this case, we will stop moving the pointers as arr1[] and arr2[] are containing correct elements.
3.  Thus, after step 2, arr1[] will contain all smaller elements and arr2[] will contain all bigger elements. Finally, we will sort the two arrays.
'''

def mergeArrays(arr1, arr2):
    
    print("arr1: ",arr1)
    print("arr2: ",arr2)
    print("********")

    n = len(arr1)
    m = len(arr2)

    ptr1 = n - 1
    ptr2 = 0

    while ptr1 >= 0 and ptr2 < m:
        # print(ptr1, ptr2)
        if arr1[ptr1] > arr2[ptr2]:
            # Swap
            arr1[ptr1], arr2[ptr2] = arr2[ptr2], arr1[ptr1]
        
        ptr1 -= 1   #Move ptr1 to left side (decrement)
        ptr2 += 1   #Move ptr2 to right side (increment)

    # Now, the two arrays have the correct elements in unsorted manner. 
    # Sort the arrays arr1 and arr2

    arr1.sort()
    arr2.sort()

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

# ? Time Complexity: O(min(n, m)) + O(nlogn) + O(mlogm), where n and m are the sizes of the given arrays.
# ? Reason:  O(min(n, m)) is for swapping the array elements. And O(n*logn) and O(m*logm) are for sorting the two arrays.
# ? Space Complexity: O(1) as we are not using additonal space.