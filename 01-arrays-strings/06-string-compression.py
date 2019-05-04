'''
Implement a method to perform basic string compression using the counts of repeated characters.
If the "compressed" string would not become smaller than the 
original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters.

aabcccccaaa -> a2b1c5a3

Time: O(n)
Space: O(n)
'''

# First Solution

def compute_compressed_length_01(string):
    if string is None:
        return None
    if len(string) == 1:
        return 2
    compressed_length = 1
    num_dupes = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            num_dupes += 1
        else:
            compressed_length += 1 + len(str(num_dupes))
            num_dupes = 1
    return compressed_length

def string_compression_01(string):
    if string is None:
        return None
    if len(string) <= compute_compressed_length_01(string):
        return string
    compressed = string[0]
    num_dupes = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            num_dupes += 1
        else:
            compressed += str(num_dupes) + string[i]
            num_dupes = 1
    compressed += str(num_dupes)
    return compressed

# Second Solution

def string_compression_02(string):
    if string is None:
        return None
    compressed = ''
    num_dupes = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            num_dupes += 1
        else:
            compressed += string[i] + str(num_dupes)
            num_dupes = 1
    i += 1
    compressed += string[i] + str(num_dupes)
    if len(compressed) > len(string):
        return string
    else:
        return compressed

# Test

if __name__ == '__main__':
    s = input().rstrip()
    print(string_compression_01(s))
    print(string_compression_02(s))