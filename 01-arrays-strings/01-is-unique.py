# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Time: O(n)
# Space: O(1)

def is_unique_0(s):
    hash_table = [False]*128
    for l in s:
        ind = ord(l)
        if hash_table[ind]:
            return False
        hash_table[ind] = True
    return True

# Time: O(n^2)
# Space: O(1)

def is_unique_1(s):
    l = len(s)
    for base in range(l-1):
        for ind in range(base, l):
            if s[base] == s[ind]:
                return False
    return True

# Time: O(nlog(n))
# Space: O(n) [strings in Python are immutable]

def is_unique_2(s):
    l = len(s)
    new = ''.join(sorted(s.split()))
    for ind in range(1, l):
        if new[ind] == new[ind-1]:
            return False
    return True

# Test

if __name__ == "__main__":
    print(is_unique_0(input().rstrip()))
    print(is_unique_1(input().rstrip()))
    print(is_unique_2(input().rstrip()))