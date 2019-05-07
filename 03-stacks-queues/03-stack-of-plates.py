from Stack import Stack

class SetOfStacks:
    def __init__(self, max_height):
        self.max_height = max_height
        self.stacks = [Stack()]
        self.i = 0

    def push(self, value):
        if self.stacks[self.i].size == self.max_height:
            self.stacks.append(Stack())
            self.i += 1
        self.stacks[self.i].push(value)

    def pop(self):
        if self.stacks[self.i].is_empty():
            return None
        value = self.stacks[self.i].pop()
        if self.stacks[self.i].is_empty() and self.i != 0:
            self.stacks.pop()
            self.i -= 1
        return value
    
    def pop_at(self, index):
        if  index < 0 or index > self.i:
            return None
        if self.stacks[index].is_empty():
            return None
        value = self.stacks[index].pop()
        if self.stacks[index].is_empty() and index != 0:
            self.stacks.pop(index)
            self.i -= 1
        return value
