# Given a string, write a function to check if it is a permutation of a palindrome.

# "tact coa" -> True (permutations: "tacocat", "atcocta", etc.)

# Time: O(n)
# Space: O(1)

def palindrome_permutation(string):
    if string is None:
        return True
    bit_vector = [False] * 26
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            bit_vector[ord(char) - ord('a')] = not bit_vector[ord(char) - ord('a')]
        if ord('A') <= ord(char) <= ord('Z'):
            bit_vector[ord(char) - ord('A')] = not bit_vector[ord(char) - ord('A')]
    return sum(bit_vector) <= 1

# Test

if __name__ == '__main__':
    s = input().rstrip()
    print(palindrome_permutation(s))