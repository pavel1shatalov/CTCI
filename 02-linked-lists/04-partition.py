'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x
(see below).The partition element x can appear anywhere in the "right partition"; it does not need to appear between
the left and right partitions.

Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Time: O(n)
Space: O(1)
'''

from LinkedList import LinkedList

def partition(node, k):
    head = tail = node
    while node:
        next_node = node.next
        node.next = None # because the last element has to point to None
        if node.data >= k:
            tail.next = node
            tail = node
        else:
            if node is not head: # be careful with node.next = node
                node.next = head
            head = node
        node = next_node
    return head

# Modified version: the partition element is right between the partitions
# Time: O(n)
# Space: O(1)

def partition_modified(lst, k):
    curr = lst.head
    partition_element = lst.find(k)
    if partition_element:
        head = tail = partition_element
    else:
        head = tail = curr
    lst.remove_first(k)
    while curr:
        next_node = curr.next
        curr.next = None # because the last element has to point to None
        if curr.data >= k:
            tail.next = curr
            tail = curr
        else:
            if curr is not head: # be careful with curr.next = curr
                curr.next = head
            head = curr
        curr = next_node
    lst.head = head

# Test

if __name__ == '__main__':

    lst = LinkedList()
    lst.append(3)
    lst.append(5)
    lst.append(8)
    lst.append(5)
    lst.append(10)
    lst.append(2)
    lst.append(1)
    print(lst)
    # It's important to check for k < min(lst) and for k > max(lst)
    lst.head = partition(lst.head, 5)
    print(lst)
    partition_modified(lst, 5)
    print(lst)
    