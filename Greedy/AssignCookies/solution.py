'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. 
If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''


def assignCookies(g, s):
    g.sort()
    s.sort()
    n = len(g)
    m = len(s)
    l = 0
    r = 0
    while l < n and r < m:
        if g[l] <= s[r]:
            l += 1
        r += 1
    
    return l

# Main
g = [1, 5, 3, 3, 4]
s = [4, 2, 1, 2, 1, 3]

print(assignCookies(g, s))

# ? Time Complexity : O(NlogN) + O(MlogM) + O(N) where N is size of greed array and M is size of size array
# ?                   This is because we are sorting both the arrays and the while loop runs for O(N) time as the loop exits when the array is traversed completely.


