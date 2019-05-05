from LinkedList import LinkedList

# Time: O(n)
# Space: O(1)

def return_kth_to_last(head, k):
    if k <= 0:
        return None
    fast = head
    slow = head
    for i in range(k):
        if fast.next is None and i < k - 1:
            return None
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow

# Test

if __name__ == '__main__':

    lst = LinkedList()
    for i in range(5):
        lst.append(i)
    print(lst)
    print(return_kth_to_last(lst.head, 3))