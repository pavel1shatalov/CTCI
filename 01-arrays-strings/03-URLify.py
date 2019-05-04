'''
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the
"true" length of the string.

'Mr. John Smith' -> 'Mr.%20John%20Smith%20'

Time: O(n)
Space: O(n)
In Python strings are immutable, thus we are forced to implement with lists of single characters.
'''

def URLify(string):
    new_len = 0
    for char in string:
        if char == ' ':
            new_len += 3
        else:
            new_len += 1
    reader = len(string) - 1
    string += [' '] * (new_len - len(string))
    writer = len(string) - 1
    while reader >= 0 and writer >= 0:
        if string[reader] == ' ':
            string[writer] = '0'
            string[writer - 1] = '2'
            string[writer - 2] = '%'
            writer -= 3
            reader -= 1
        else:
            string[writer] = string[reader]
            writer -= 1
            reader -= 1
    return string

# Test

if __name__ == '__main__':
    s = input().rstrip()
    output = ''.join(URLify(list(s)))
    print(output)