'''
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. 
In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, 
and their sum is equal to zero.
'''

def threeSum(arr):
    n = len(arr)
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    triplets.add(tuple(temp))
    
    triplets = list(triplets)
    return triplets

# Main
arr = [-1, 0, 1, 2, -1, -4]
print("Triplets are :", threeSum(arr))

# ? Time Complexity: O(N^3 * log(number of unique triplets))
# ?                  Here, we are mainly using 3 nested loops. And inserting triplets into the set 
# ?                  takes O(log(no. of unique triplets)) time complexity. 
# ?                  But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

# ? Space Complexity: O(2 * number of unique triplets) as we are using a set data structure 
# ?                   and a list to store the triplets and extra O(N) for storing the array elements in another set.