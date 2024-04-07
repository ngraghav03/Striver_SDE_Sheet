'''
Problem Statement: Given a String, find the length of longest substring without any repeating character.
'''

def longestSubstringWithoutRepetition(str):

    n = len(str)
    maxLength = 1

    sett = set()
    l = 0
    for r in range(n):
        if str[r] in sett:
            while l < r and str[r] in sett:
                sett.remove(str[l])
                l += 1
        
        sett.add(str[r])
        maxLength = max(maxLength, r - l + 1)
    
    return maxLength

# Main
s = "abcabcbb"
s1 = "bbbbb"

print(longestSubstringWithoutRepetition(s))
print(longestSubstringWithoutRepetition(s1))

# ? Time Complexity: O(2*N) as in the worst case, both left and right have to travel the complete array.
# ? Space Complexity: O(N) as we are storing at most N elements in the hashSet.
