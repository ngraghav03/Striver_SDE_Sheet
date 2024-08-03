'''
Problem Statement: Given N and K, where N is the sequence of numbers from 1 to N([1,2,3..... N]) find the Kth permutation sequence.
'''

class Solution:
    def getPermutation(self, n, k):
        fact = 1
        numbers = []
        for i in range(1, n):
            fact *= i
            numbers.append(i)
        numbers.append(n)

        ans = ""
        k = k - 1
        while True:
            print("n = ", len(numbers), "k = ", k)
            ans += str(numbers[k // fact])
            numbers.pop(k // fact)

            if len(numbers) == 0:
                break

            # Update k
            k = k % fact
            fact = fact // len(numbers)
        
        return ans

# Main
n1 = 3
k1 = 3

n2 = 4
k2 = 17

obj = Solution()
print("Required permutation for n = ", n1, "and k = ", k1, "is ", obj.getPermutation(n1, k1))
print("Required permutation for n = ", n2, "and k = ", k2, "is ", obj.getPermutation(n2, k2))

# ? Time Complexity: O(N) * O(N) = O(N^2)
# ?                  Reason: We are placing N numbers in N positions. This will take O(N) time. 
# ?                  For every number, we are reducing the search space by removing the element already placed in the previous step. This takes another O(N) time.

# ? Space Complexity: O(N) + O(N) = O(2N) ~ O(N)
# ?                   Reason: O(N) for the array containing numbers 1 to N and O(N) for storing the answer permutation