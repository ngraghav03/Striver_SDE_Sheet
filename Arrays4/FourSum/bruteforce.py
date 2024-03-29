'''
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, 
you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.
'''

def fourSum(arr, target):
    n = len(arr)
    quadruplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        quadruplets.add(tuple(temp))
    
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

# ? Time Complexity: O(N^4) as we are using 4 nested loops.
# ?                  More precisely, O(N^4 * no.of unique quadruplets), but we can write it as O(N^4)

# ? Space Complexity:  O(2 * no. of quadruplets), as we are using both a set and list to store the answer. 