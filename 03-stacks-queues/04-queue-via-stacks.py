# Time:
#   -> enqueue: O(1)
#   -> dequeue: O(1) amortized
# Space: O(N)

from Stack import Stack

class MyQueue:
    def __init__(self):
        self.size = 0
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        self.size += 1
        self.s1.push(value)
    
    def dequeue(self):
        self.size -= 1
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()
    
    def front(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()
    