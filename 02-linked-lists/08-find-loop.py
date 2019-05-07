'''
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. 

Input: A -> B -> C -> D -> E -> C [the same C as earlier] 
Output: C

Time: O(n)
Space: O(1)
'''

from LinkedList import LinkedList, Node

def find_loop(lst):
    fast = slow = lst.head
    while fast and slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    else:
        return None
    slow = lst.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast

# Test

if __name__ == '__main__':

    lst = LinkedList()
    node = Node('C')
    lst.append('A')
    lst.append('B')
    lst.append_node(node)
    lst.append('D')
    lst.append('E')
    lst.append_node(node)
    print(find_loop(lst))