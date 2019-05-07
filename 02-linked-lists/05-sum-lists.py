'''
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function
that adds the two numbers and returns the sum as a linked list.

Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: (2 -> 1 -> 9). That is, 912.

Time: O(n)
Space: O(n)
'''

from LinkedList import LinkedList, Node

def sum_lists_iterative(lst1, lst2):
    lst = LinkedList()
    curr1 = lst1.head
    curr2 = lst2.head
    carry = False
    while curr1 or curr2 or carry:
        if carry:
            data = 1
            carry = False
        else:
            data = 0
        if curr1:
            data += curr1.data
            curr1 = curr1.next
        if curr2:
            data += curr2.data
            curr2 = curr2.next
        if data >= 10:
            carry = True
        node = Node(data % 10)
        if lst.head is None:
            head = node
            lst.head = head
        else:
            lst.head.next = node
            lst.head = node
    lst.head = head
    return lst

def sum_lists_recursive(node1, node2, carry=False):
    if (node1 is None and node2 is None and carry is False):
        return None
    if carry:
        data = 1
        carry = False
    else:
        data = 0
    if node1:
        data += node1.data
    if node2:
        data += node2.data
    if data >= 10:
        carry = True
    node = Node(data % 10)
    node.next = sum_lists_recursive(node1.next, node2.next, carry)
    return node

# Test

if __name__ == '__main__':

    lst1 = LinkedList()
    lst1.append(7)
    lst1.append(1)
    lst1.append(6)
    lst2 = LinkedList()
    lst2.append(5)
    lst2.append(9)
    lst2.append(2)
    print(lst1)
    print(lst2)
    lst_iterative = sum_lists_iterative(lst1, lst2)
    lst_recursive = LinkedList()
    lst_recursive.head = sum_lists_recursive(lst1.head, lst2.head)
    print(lst_iterative)
    print(lst_recursive)
