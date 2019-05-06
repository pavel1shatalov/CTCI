# Implementation of SinglyLinkedList in Python with time complexities

class Node:
    # O(1)
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    # O(1)
    def __init__(self, head=None):
        self.head = head

    # O(n)
    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    # O(1)
    def prepend(self, data):
        self.head = Node(data, self.head)
    
    # O(n)
    def append(self, data):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        else:
            self.head = Node(data)

    # O(1)
    def pop_head(self):
        head = self.head
        if head:
            self.head = self.head.next
        return head

    # O(n)
    def pop_tail(self):
        curr = self.head
        if curr is None:
            return None
        if curr.next is None:
            self.head = None
            return curr
        while curr.next.next:
            curr = curr.next
        tail = curr.next
        curr.next = tail.next
        return tail

    # O(n)
    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr
    
    # O(n)
    def remove_first(self, key):
        if self.head and self.head.data == key:
            self.head = self.head.next
            return
        curr = self.head
        while curr and curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
                return
            else:
                curr = curr.next  

    # O(n)
    def remove(self, key):
        while self.head and self.head.data == key:
            self.head = self.head.next
        curr = self.head
        while curr and curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # O(n)
    def reverse(self, key):
        curr_node = self.head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        