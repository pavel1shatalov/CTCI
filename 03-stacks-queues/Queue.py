class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class Queue:
    def __init__(self, front=None):
        self.size = 0
        self.front = front
        self.back = front

    def peek_front(self):
        return self.front

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, value):
        self.size += 1
        node = Node(value)
        if self.back is not None:
            self.back.next_node = node
            self.back = node
        else:
            self.front = node
            self.back = node

    def dequeue(self, value):
        self.size -= 1
        node = self.front
        if self.front is self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next_node
        return node