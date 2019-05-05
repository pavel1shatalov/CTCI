'''
Assume you have a method is_substring() which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to is_substring().

string_rotation("waterbottle", "erbottlewat")

Time: O(n)
Space: O(n)
'''

def is_substring(s1, s2):
    return s1 in s2

def string_rotation(s1, s2):
    return is_substring(s2, s1 + s1)

if __name__ == '__main__':
    output = string_rotation("waterbottle", "erbottlewat")
    print(output)