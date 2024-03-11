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
Algorithm:
1. First, assume the two arrays as a single array and calculate the gap value i.e. ceil((size of arr1[] + size of arr2[]) / 2).
2. We will perform the following operations for each gap until the value of the gap becomes 0:
    1. Place two pointers in their correct position like the left pointer at index 0 and the right pointer at index (left+gap).
    2. Again we will run a loop until the right pointer reaches the end i.e. (n+m). Inside the loop, there will be 3 different cases:
        1. If the left pointer is inside arr1[] and the right pointer is in arr2[]: We will compare arr1[left] and arr2[right-n] and swap them if arr1[left] > arr2[right-n].
        2. If both the pointers are in arr2[]: We will compare arr1[left-n] and arr2[right-n] and swap them if arr1[left-n] > arr2[right-n].
        3. If both the pointers are in arr1[]: We will compare arr1[left] and arr2[right] and swap them if arr1[left] > arr2[right].
    3. After the right pointer reaches the end, we will decrease the value of the gap and it will become ceil(current gap / 2). 
3. Finally, after performing all the operations, we will get the merged sorted array.
'''

def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def merge(arr1, arr2, n, m):
    # len of the imaginary single array:
    len = n + m

    # Initial gap:
    gap = (len // 2) + (len % 2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < len:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)

if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    merge(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print()

# ? Time Complexity: O((n+m)*log(n+m)), where n and m are the sizes of the given arrays.
# ? Reason: The gap is ranging from n+m to 1 and every time the gap gets divided by 2. 
# ? So, the time complexity of the outer loop will be O(log(n+m)). Now, for each value of the gap, the inner loop can at most run for (n+m) times. 
# ? So, the time complexity of the inner loop will be O(n+m). So, the overall time complexity will be O((n+m)*log(n+m)).

# ? Space Complexity: O(1) as we are not using any extra space.

