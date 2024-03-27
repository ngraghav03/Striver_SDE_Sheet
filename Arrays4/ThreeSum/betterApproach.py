'''
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. 
In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, 
and their sum is equal to zero.
'''

def threeSum(arr):
    triplets = set()
    n = len(arr)

    for i in range(n):
        hashSet = set()
        for j in range(i + 1, n):
            requiredThirdNo = (-1) * (arr[i] + arr[j])

            if requiredThirdNo in hashSet:
                temp = [arr[i], arr[j], requiredThirdNo]
                temp.sort()
                triplets.add(tuple(temp))
            else:
                hashSet.add(arr[j])
    
    ans = list(triplets)
    return ans

# Main
arr = [-1, 0, 1, 2, -1, -4]
print("Triplets are :", threeSum(arr))

# ? Time Complexity: O(N^2 * log(number of unique triplets))
# ?                  Here, we are mainly using 2 nested loops. And inserting triplets into the set 
# ?                  takes O(log(no. of unique triplets)) time complexity. 
# ?                  But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

# ? Space Complexity: O(2 * number of unique triplets) as we are using a set data structure 
# ?                   and a list to store the triplets and extra O(N) for storing the array elements in another set.
