'''
Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).
What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].
'''

def countInversions_mergeSort(arr):
    n = len(arr)
    return mergeSort(arr, 0, n - 1)

def mergeSort(arr, low, high):
    count = 0
    if low >= high:
        return count
    
    mid = (low + high) // 2
    count += mergeSort(arr, low, mid)
    count += mergeSort(arr, mid + 1, high)
    count += merge(arr, low, mid, high)

    return count

def merge(arr, low, mid, high): 
    temp = []   # temporary array
    left = low  # starting index of left half of array
    right = mid + 1   # starting index of right half of array
    count = 0       # Modification 1: count variable to count the pairs

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1

        elif arr[left] > arr[right]:
            temp.append(arr[right])
            right += 1
            count += (mid - left) + 1   # Modification 2: If left array element is greater, update count
    
    # If elements on left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # If elements on right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # Transferring all elements from temporary array temp to original array arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    
    return count


# Main
array = [1,2,3,4,5]
array1 = [2,1,4,3,5]

print(countInversions_mergeSort(array2))

# ? Time Complexity: O(NlogN) as we do Merge Sort
# ? Space Complexity: O(N) as we make use of a temporary array of size N to store the elements in sorted order.