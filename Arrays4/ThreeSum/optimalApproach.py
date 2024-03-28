'''
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. 
In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, 
and their sum is equal to zero.
'''

def threeSum(arr):
    n = len(arr)
    
    arr.sort()
    ans = []

    for i in range(n):
        # Skipping iterations for i value same as previous i value.
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        
        # Initialize two pointers j and k
        j = i + 1
        k = n - 1

        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == 0:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(tuple(temp))
                # Increment j pointer and decrement k pointer
                j += 1
                k -= 1
                
                # Skip those iterations for which current j is same as previous j
                while j < k and arr[j] == arr[j - 1]:
                    j += 1

                # Skip those iterations for which current k is same as previous k
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

            elif sum < 0:
                # If sum < 0, we need a greater value to get to sum 0
                j += 1
            
            else:
                # If sum < 0, we need a smaller value to get to sum 0
                k -= 1
    return ans

# Main
arr = [-1, 0, 1, 2, -1, -4]
print("Triplets are :", threeSum(arr))

# ? Time Complexity: O(NlogN) + O(N^2) as O(NlogN) is for sorting the array.
# ?                  The pointer i, is running for approximately N times. 
# ?                  And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. 
# ?                  So the total time complexity will be O(N2). 

# ? Space Complexity: O(number of unique triplets) as we are storing the triplets.
# ?                   The space is only used to store the answer. We are not using any extra space.
# ?                   So in that perspective, space complexity can be written as O(1).