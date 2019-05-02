def search_insertion(s1, s2):
    i1 = 0
    i2 = 0
    difference_found = False
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            if difference_found:
                return False
            difference_found = True
            if len(s1) > len(s2):
                i1 += 1
            else:
                i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True

def search_replacement(s1, s2):
    difference_found = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if difference_found:
                return False
            difference_found = True
        i += 1
    return True



def one_away(s1, s2):
    len_difference = abs(len(s1) - len(s2))
    if len_difference > 1:
        return False
    if len_difference == 1:
        return search_insertion(s1, s2)
    return search_replacement(s1, s2)