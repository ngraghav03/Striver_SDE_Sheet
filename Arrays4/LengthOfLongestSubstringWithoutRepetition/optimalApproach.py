'''
Problem Statement: Given a String, find the length of longest substring without any repeating character.
'''

def longestSubstringWithoutRepetition(str):

    n = len(str)
    maxLength = 1

    sett = set()
    # left pointer is initialized to 0 and we run a loop through r from 0 to n - 1
    l = 0
    for r in range(n):
        if str[r] in sett:
            # If the character is present in the hashSet already, then remove str[left] till the repeating character is removed
            # and increment the left pointer
            while l < r and str[r] in sett:
                sett.remove(str[l])
                l += 1

        # If the character is not in the hashset, then add it to the hashset
        sett.add(str[r])
        # Update maxLength according to the newest l and r pointers
        maxLength = max(maxLength, r - l + 1)
    
    return maxLength

# Main
s = "abcabcbb"
s1 = "bbbbb"

print(longestSubstringWithoutRepetition(s))
print(longestSubstringWithoutRepetition(s1))

# ? Time Complexity: O(2*N) as in the worst case, both left and right have to travel the complete array.
# ? Space Complexity: O(N) as we are storing at most N elements in the hashSet (if all elements are unique).
