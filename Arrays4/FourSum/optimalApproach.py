'''
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, 
you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.
'''
def fourSum(arr, target):
    n = len(arr) 
    
    arr.sort()
    ans = []

    for i in range(n):
        # Skip those iterations where previous element = current element
        if i != 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):
            # Skip those iterations where previous element = current element
            if j != (i + 1) and arr[j] == arr[j - 1]:
                continue

            # i and j are the fixed pointers.
            # Initialize the two moving pointers
            k = j + 1
            l = n - 1

            while k < l:
                sum = arr[i] + arr[j] + arr[k] + arr[l]
                if sum == target:
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    ans.append(temp)
                    # Increment k and decrement l
                    k += 1
                    l -= 1

                    while k < l and arr[k] == arr[k - 1]:
                        # Skip those iterations where the previous arr[k] = current[k] 
                        # as we have already computed quadruplets corresponding to that element
                        k += 1

                    while k < l and arr[l] == arr[l + 1]:
                        # Skip those iterations where the previous arr[l] = current[l] 
                        # as we have already computed quadruplets corresponding to that element
                        l -= 1
                
                elif sum < target:
                    # We need a greater sum to get to 0
                    k += 1
                
                else:
                    # We need a smaller sum to get to 0
                    l -= 1
    
    return ans

# Main
arr1 = [1,0,-1,0,-2,2]
target1 = 0

arr2 = [4,3,3,4,4,2,1,2,1,1]
target2 = 9

print(arr1, "target = ", target1)
print("Quadruplets : ", fourSum(arr1, target1))
print(arr2, "target = ", target2)
print("Quadruplets : ", fourSum(arr2, target2))

# ? Time Complexity: O(N^3). Each of the pointers i and j, is running for approximately N times. 
# ?                          And both the pointers k and l combined can run for approximately N times 
# ?                          including the operation of skipping duplicates. So the total time complexity will be O(N^3).

# ? Space Complexity:  O(no. of quadruplets), This space is only used to store the answer. 
# ?                    We are not using any extra space to solve this problem. 
# ?                    So, from that perspective, space complexity can be written as O(1).


        
                