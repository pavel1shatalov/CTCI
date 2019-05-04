# Given two strings, write a method to decide if one is a permutation of the other.

# Time: O(n)
# Space: O(1)

def are_permutations(s1, s2):
    if len(s1) != len(s2):
        return False
    hash_table = [0] * 128
    for let in s1:
        ind = ord(let)
        hash_table[ind] += 1
    for let in s2:
        ind = ord(let)
        hash_table[ind] -= 1
        if hash_table[ind] < 0:
            return False
    return True

# Test

if __name__ == '__main__':
    s1 = input().rstrip()
    s2 = input().rstrip()
    print(are_permutations(s1, s2))