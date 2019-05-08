class TripleStack:
    def __init__(self, size=15):
        self.array = [None] * size
        self.i = [0, size * 1/3, size * 2/3]
        self.min_i = [0, size * 1/3, size * 2/3]
        self.max_i = [size * 1/3 - 1, size * 2/3 - 1, size - 1]
    
    def push(self, s, value):
        if s not in [0, 1, 2]:
            return False
        if self.i[s] < self.max_i[s]:
            self.array[self.i[s]] = value
            self.i[s] += 1
        else:
            self.array[self.i[s]] = value
            gap = self.max_i[s] - self.min_i[s]
            new_stack = self.array[self.min_i[s] : self.max_i[s] + 1] + [None] * gap
            if s == 0:
                self.array = new_stack + self.array[self.min_i[1] : self.max_i[2] + 1]
                self.min_i[1:] = [x + gap for x in self.min_i[1:]]
                self.max_i[:] = [x + gap for x in self.max_i]
                self.i[0] += 1
                self.i[1:] = [x + gap for x in self.i[:1]]
            elif s == 1:
                self.array = self.array[self.min_i[0] : self.max_i[0]] + new_stack + self.array[self.min_i[2] : self.max_i[2] + 1]
                self.min_i[2] += gap
                self.max_i[1:] = [x + gap for x in self.max[1:]]
                self.i[1] += 1
                self.i[2] += gap
            else:
                self.array = self.array[self.min_i[0] : self.max_i[1] + 1] + new_stack
                self.max_i[s] += gap
                self.i[2] += 1
        return True
    
    def pop(self, s):
        if s not in [0, 1 , 2]:
            return None
        value = self.array[self.i[s]]
        self.i[s] -= 1
        return value
        
