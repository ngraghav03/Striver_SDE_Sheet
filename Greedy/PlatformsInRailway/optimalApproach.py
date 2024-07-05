'''
Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. 
We need to find the minimum number of platforms needed at the railway station so that no train has to wait.
'''

def countPlatforms(n, arr, dep):
    i = 1
    j = 0
    platforms = 1
    count = 1

    arr.sort()
    dep.sort()

    while (i < n and j < n):
            
            if (arr[i] <= dep[j]):
                i += 1
                count += 1
            
            elif (arr[i] > dep[j]):
                j += 1
                count -= 1
            
            platforms = max(platforms, count)
        
    return platforms


# Main
arr1 = [900, 945, 955, 1100, 1500, 1800]
dep1 = [920, 1200, 1130, 1150, 1900, 2000]
n1 = len(dep1)
print("Minimum number of Platforms required = ", countPlatforms(n1, arr1, dep1))

arr2 = [1020, 1200]
dep2 = [1050, 1230]
n2 = len(dep2)
print("Minimum number of Platforms required = ", countPlatforms(n2, arr2, dep2))

# ? Time Complexity: O(N^2)  (due to two nested loops).

# ? Space Complexity: O(1)  (no extra space used).