'''
There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false

Time: O(n)
Space: O(1)
'''

def one_away(s1, s2):
    len_difference = abs(len(s1) - len(s2))
    if len_difference > 1:
        return False
    i1 = i2 = 0
    difference_found = False
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            if difference_found:
                return False
            difference_found = True
            if len(s1) > len(s2):
                i1 += 1
            elif len(s1) < len(s2):
                i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True

# Test

if __name__ == '__main__':
    s1 = input().rstrip()
    s2 = input().rstrip()
    print(one_away(s1, s2))