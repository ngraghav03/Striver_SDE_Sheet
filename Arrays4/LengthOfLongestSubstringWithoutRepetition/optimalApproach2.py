'''
Problem Statement: Given a String, find the length of longest substring without any repeating character.
'''

def longestSubstringWithoutRepetition(str):

    n = len(str)
    maxLength = 0
    length = 0
    hashMap = {}
    # left pointer is initialized to 0 and we run a loop through r from 0 to n - 1
    l = 0

    for r in range(n):
        
        if str[r] in hashMap:
            # Check if the latest index of that character is in range/window [l..r]
            # If yes, then move l to that index + 1. 
            # Else, just update it to r
            if hashMap[str[r]] >= l and hashMap[str[r]] <= r:   #second condition is not needed but added for understanding
                l = hashMap[str[r]] + 1
                hashMap[str[r]] = r
                maxLength = max(maxLength, r - l + 1)
                
            else:
                hashMap[str[r]] = r
                maxLength = max(maxLength, r - l + 1)
                
            # ? Note we can collectively update our hashMap[str[r]] = r by commonly writing it outside of if and else blocks

        else:
            hashMap[str[r]] = r
            maxLength = max(maxLength, r - l + 1)
 
    return maxLength

# Main
s = "abcabcbb"
s1 = "bbbbb"
s2 = "takeUforward"

print(longestSubstringWithoutRepetition(s))
print(longestSubstringWithoutRepetition(s1))
print(longestSubstringWithoutRepetition(s2))

# ? Time Complexity: O(N) as only the right pointer travels the complete array and left makes direct jumps instead of moving one-by-one
# ? Space Complexity: O(N) as we are storing at most N elements in the hashMap (if all elements are unique).
