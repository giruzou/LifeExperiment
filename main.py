from random import randrange

class Animal(object):
    def __init__(self):
        self.age = 0

    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_pos(self):
        return (self.x, self.y)

    def get_age(self):
        return self.age

    def add_age(self):
        if self.limit > self.age:
            self.age += 1
        else:
            self.age = -2

class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.limit = 10

class Rat(Animal):
    def __init__(self):
        super(Rat, self).__init__()
        self.limit = 10

class Rat(Animal):
    def __init__(self):
        super().__init__()
        self.limit = 2
    
class Field(object):
    def __init__(self):
        self.animals = []
        self.size = 100

    def add(self, ani):
        self.animals.append(ani)

    def add_age(self):
        for animal in self.animals:
            animal.add_age()

    def delete_dead(self):
       self.animals = [animal for animal in self.animals if animal.age >= 0] 

    def print_age(self):
        for animal in self.animals:
            print(animal.get_age())
    
    def animals_sort(self):
    	base = lambda animal: animal.x * self.size + animal.y
    	self.animals = sorted(self.animals, key=base)
    	for animal in self.animals:
    		print base(animal)

field = Field()
for i in range(100):
    animal = Cat()
    animal.set_pos(randrange(field.size), randrange(field.size))
    field.add(animal)

field.animals_sort()
'''
for i in range(11):
     field.add_age()
field.print_age()
print(len(field.animals))
field.delete_dead()
print(len(field.animals))
'''