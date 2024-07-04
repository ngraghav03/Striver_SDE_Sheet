'''
Problem Statement: We are given two arrays that represent the arrival and departure times of trains that stop at the platform. 
We need to find the minimum number of platforms needed at the railway station so that no train has to wait.
'''

def countPlatforms(n, arr, dep):
    platforms = 1

    for i in range(n):
        count = 1

        for j in range(i + 1, n):
            
            # We need another platform if a train with arrival between arr[i] and dep[i] or when a train is parked after arr[i].
            # i.e., we need a train with arrival before arr[i] and departure after arr[i] -> condition 2 -- the train is just parked after arr[i]
            #  or we need a train with arrival after arr[i]

            # ^ -------------|------------------|---
            # ? ------|---------------------|---
            # ! ---------|----------------|------ i
            if ((arr[i] >= arr[j] and arr[i] <= dep[j]) or (arr[j] >= arr[i] and arr[j] <= dep[i])):        # * 1st condition is blue case and 2nd condition is yellow case
                count += 1

        platforms = max(platforms, count)
    
    return platforms

            

# Main
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
n = len(dep)
print("Minimum number of Platforms required = ", countPlatforms(n, arr, dep))

# ? Time Complexity: O(N^2)  (due to two nested loops).

# ? Space Complexity: O(1)  (no extra space used).