'''
Problem Statement:
Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].

Example 1:
Input: N = 5, array[] = {1,3,2,3,1)
Output: 2 
Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.

Example 2:
Input: N = 4, array[] = {3,2,1,4}
Output: 1
Explaination: There is only 1 pair  ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j]
'''

def mergeSort(arr, low, high):
    # count = 0
    # if low >= high:
    #     return count
    # mid = (low + high) // 2
    # count += mergeSort(arr, low, mid)
    # count += mergeSort(arr, mid + 1, high)
    # count += merge(arr, low, mid, high)
    # return count

    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += mergeSort(arr, low, mid)  # left half
    count += mergeSort(arr, mid + 1, high)  # right half
    count += countPairs(arr, low, mid, high)  # Modification
    # count += merge(arr, low, mid, high)  # merging sorted halves
    merge(arr, low, mid, high)
    return count

def merge(arr, low, mid, high):
    # count = 0
    # left = low
    # right = mid + 1

    # # Calculating count
    # for i in range(low, mid + 1):
    #     while ((arr[i] > (2 * arr[right])) and right <= high):
    #         right += 1
    #     count = count + (right - (mid + 1)) 
        

    # Merging
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    
    # return count

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

# Main
l = [40, 25, 19, 12, 9, 6, 2]
n = len(l)
print(mergeSort(l, 0, n - 1))
    

