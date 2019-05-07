# Time: O(n)
# Space: O(n)

from LinkedList import LinkedList

def palindrome(head):
    curr = head
    size = 0
    while curr:
        size += 1
        curr = curr.next
    curr = head
    half = size // 2
    new = None
    for _ in range(half):
        next_node = curr.next
        curr.next = new
        new = curr
        curr = next_node
    if size % 2:
        curr = curr.next
    while curr and new:
        if curr.data != new.data:
            return False
        curr = curr.next
        new = new.next
    return True

# Test

if __name__ == '__main__':

    lst = LinkedList()
    lst.append(4)
    lst.append(3)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    print(lst)
    print(palindrome(lst.head))
