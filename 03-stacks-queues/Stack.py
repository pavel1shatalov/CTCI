class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def push(self, value):
        node = Node(value, self.head)
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        tmp = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return tmp

    def __str__(self):
        string_list = [] # appending: O(1) amortized
        temp = self.head
        while temp is not None:
            string_list += [str(temp.value)]
            temp = temp.next_node
        return " ".join(string_list)