# Time: O(n^2)
# Space: O(2n)

from Stack import Stack


def sort_stack(s1):
    s2 = Stack()
    while not s1.is_empty():
        tmp = s1.pop()
        while not s2.is_empty() and s2.peek() > tmp:
            s1.push(s2.pop())
        s2.push(tmp)
    return s2
