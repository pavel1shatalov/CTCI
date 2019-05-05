'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
than or equal to x. lf x is contained within the list, the values of x only need to be after the elements less than x
(see below).The partition element x can appear anywhere in the "right partition"; it does not need to appear between
the left and right partitions.

Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8    CHANGE EXAMPLE FROM THE BOOK

Time: O(n)
Space: O(1)
'''

# ADD TEST

from LinkedList import LinkedList

def partition(node, k):
    tail = node
    head = node
    while node is not None:
        nextNode = node.next_node
        node.next_node = None
        if node.value >= k:
            tail.next_node = node
            tail = node
        else:
            node.next_node = head
            head = node
        node = nextNode
    return head
    