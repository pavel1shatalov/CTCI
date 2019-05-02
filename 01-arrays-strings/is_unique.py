def is_unique0(s):
    hash_table = [False]*128
    for l in s:
        ind = ord(l)
        if hash_table[ind]:
            return False
        hash_table[ind] = True
    return True

def is_unique1(s):
    l = len(s)
    for base in range(l-1):
        for ind in range(base, l):
            if s[base] == s[ind]:
                return False
    return True

def is_unique2(s):
    l = len(s)
    new = ''.join(sorted(s.split()))
    for ind in range(1, l):
        if new[ind] == new[ind-1]:
            return False
    return True

if __name__ == "__main__":
    print(is_unique0(input().rstrip()))
    print(is_unique1(input().rstrip()))
    print(is_unique2(input().rstrip()))