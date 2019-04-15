def URLify(string):
    new_len = 0
    reader = len(string) - 1
    for char in string:
        if char == ' ':
            new_len += 3
        else:
            new_len += 1
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

print(URLify(list(input())))