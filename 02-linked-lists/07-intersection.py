'''
Given two singly linked lists, determine if they intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. That is, if the kth node of the 
first linked list is the exact same node (by reference) as the jth node of the second linked list, 
then they are intersecting.

3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1 
                    ^
                    |
               4 -> 9  

Time: O(n)
Space: O(1)
'''

from LinkedList import LinkedList, Node

def intersection(lst1, lst2):
    size1 = 0
    size2 = 0
    curr1 = lst1.head
    curr2 = lst2.head
    while curr1:
        size1 += 1
        curr1 = curr1.next
    while curr2:
        size2 += 1
        curr2 = curr2.next
    diff = size1 - size2
    if size1 >= size2:
        fast = lst1.head
        slow = lst2.head
    else:
        fast = lst2.head
        slow = lst1.head
        diff = -diff
    for _ in range(diff):
        fast = fast.next
    while slow:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next
    return None

# Test

if __name__ == '__main__':

    lst1 = LinkedList()
    lst1.append(3)
    lst1.append(1)
    lst1.append(5)
    lst1.append(9)
    lst2 = LinkedList()
    lst2.append(4)
    lst2.append(9)
    node1 = Node(7)
    node2 = Node(2)
    node3 = Node(1)
    lst1.append_node(node1)
    lst2.append_node(node1)
    node1.next = node2
    node2.next = node3
    print(lst1)
    print(lst2)
    print(intersection(lst1, lst2))
