# Time: O(1)
# Space: O(2N)

from Stack import Stack

class StackMin(Stack):
    def __init__(self):
        super().__init__()
        self.min_stack = Stack()
    
    def push(self, value):
        super().push(value)
        if self.min_stack.is_empty() or value <= self.min_stack.peek():
            self.min_stack.push(value)
    
    def pop(self):
        value = super().pop()
        if value == self.min_stack.peek():
            return self.min_stack.pop()
        
    def peek_min(self):
        return self.min_stack.peek()
