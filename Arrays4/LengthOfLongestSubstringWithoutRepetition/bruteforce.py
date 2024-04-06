'''
Problem Statement: Given a String, find the length of longest substring without any repeating character.
'''

def longestSubstringWithoutRepetition(str):

    n = len(str)
    maxLength = 1

    for i in range(n):
        hashSet = set()
        for j in range(i, n):
            if str[j] in hashSet:
                maxLength = max(maxLength, j - i)
                break
            else:
                hashSet.add(str[j])
    
    return maxLength

# Main
s = "abcabcbb"
s1 = "bbbbb"

print(longestSubstringWithoutRepetition(s))
print(longestSubstringWithoutRepetition(s1))

# ? Time Complexity: O(N^2) as we are using two nested loops.
# ? Space Complexity: O(1) as we are not using any additional space.
