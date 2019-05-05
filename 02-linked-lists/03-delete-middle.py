# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last
# node, not necessarily the exact middle) of a singly linked list, given only access to that node.

# Time: O(1)
# Space: O(1)

from LinkedList import LinkedList, Node


def delete_middle(node):
    node.data = node.next.data
    node.next = node.next.next

# Test

if __name__ == '__main__':
    
    lst = LinkedList()

    for i in range(5):
        lst.append(i)
    lst.append(10)
    for i in range(5):
        lst.append(i)

    node = lst.find(10)
    print(node)
    print(lst)
    delete_middle(node)
    print(lst)
    