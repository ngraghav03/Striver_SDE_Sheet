'''
Problem Statement: You are given a string s, partition it in such a way that every substring is a palindrome. Return all such palindromic partitions of s.

Note: A palindrome string is a string that reads the same backward as forward.
'''

class Solution:
    def __init__(self):
        self.partitions = []
        self.partition = []
    
    def isPalindrome(self, s, start, end):
        while (start <= end):
            if (s[start] == s[end]):
                start += 1
                end -= 1
            else:
                return False

        return True

    def palindromePartitionHelper(self,ind, s, n):
        if ind == n:
            self.partitions.append(self.partition.copy())
            return
        
        for i in range(ind, n):
            if self.isPalindrome(s, ind, i):
                self.partition.append(s[ind : i + 1])
                self.palindromePartitionHelper(i + 1, s, n)
                self.partition.pop()


    def palindromPartition(self, s):
        n = len(s)
        self.palindromePartitionHelper(0, s, n)

        return self.partitions

# Main
s = "aabb"
print(Solution().palindromPartition(s))
