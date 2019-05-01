# Time: O(n)
# Space: O(1)

def return_kth_to_last(head, k):
    if k <= 0:
        return None
    slow = head
    fast = head
    for i in range(k):
        if fast is None and i < k - 1:
            return None
        fast = fast.next_node
    while fast is not None:
        slow = slow.next_node
        fast = fast.next_node
    return slow