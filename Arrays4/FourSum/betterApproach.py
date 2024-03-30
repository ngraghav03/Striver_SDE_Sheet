'''
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, 
you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.
'''

def fourSum(arr, target):
    n = len(arr)
    quadruplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            hashSet = set()
            for k in range(j + 1, n):
                requiredFourthNo = target - (arr[i] + arr[j] + arr[k])
                if requiredFourthNo in hashSet:
                    temp = [arr[i], arr[j], arr[k], requiredFourthNo]
                    temp.sort()
                    quadruplets.add(tuple(temp))
                
                # Store the current element in hashSet before moving to next element
                hashSet.add(arr[k])
    
    quadruplets = [list(x) for x in quadruplets]
    return quadruplets
        

# Main
arr1 = [1,0,-1,0,-2,2]
target1 = 0

arr2 = [4,3,3,4,4,2,1,2,1,1]
target2 = 9

print(arr1, "target = ", target1)
print("Quadruplets : ", fourSum(arr1, target1))
print(arr2, "target = ", target2)
print("Quadruplets : ", fourSum(arr2, target2))

# ? Time Complexity: O(N^3 * logM), where M = number of unique quadruplets as we are using 3 nested loops.

# ? Space Complexity:  O(2 * no. of quadruplets) + O(N), as we are using both a set and list to store the answer. 
# ?                    O(N) is used to store the array elements which is input 
# ?                    So, from that perspective, this O(N) term can be ignored.