class Animal:
    def __init__(self, name, species, order, next_node=None):
        self.name = name
        self.species = species
        self.order = order
        self.next_node = next_node

class Queue:
    def __init__(self, front=None):
        self.front = front
        self.back = front

    def push_back(self, node):
        if self.back is not None:
            self.front.next_node = node
            self.back = node
        else:
            self.front = node
            self.back = node

    def pop_front(self):
        node = self.front
        if self.front is self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next_node
        return node

class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.order = 0

    def enqueue(self, name, species):
        self.order += 1
        animal = Animal(name, species, self.order)
        if animal.species == "cat":
            self.cats.push_back(animal)
        else:
            self.dogs.push_back(animal)
        
    def dequeue_cat(self):
        return self.cats.pop_front()

    def dequeue_dog(self):
        return self.dogs.pop_front()

    def dequeue_any(self):
        if self.cats.front is not None and self.dogs.front is not None:
            if self.cats.front.order < self.dogs.front.order:
                return self.cats.pop_front()
            else:
                return self.dogs.pop_front()
        elif self.cats.front is not None:
            return self.cats.pop_front()
        elif self.dogs.front is not None:
            return self.dogs.pop_front()
        else:
            return None
