import pygame
from pygame.locals import *
import sys
import numpy

class Animal(object):
    def __init__(self):
        Animal.r = 5
        self.age = 0
        # self.visible = 40 

    def set_pos(self, new_pos):
        self.pos = new_pos

    def get_pos(self):
        return self.pos

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
        Cat.color = (255, 0, 0)
        Cat.visible = 40

    def display(self, screen):
       pygame.draw.circle(screen, Cat.color, [int(self.pos[0]), int(self.pos[1])], Animal.r)

    def decide_dir(self, lst):
        res = numpy.zeros(2)
        for animal in lst:
            offset = self.pos - animal.pos
            norm = numpy.linalg.norm(offset)
            if norm < Cat.visible and norm != 0:
                res += offset / norm
        norm = numpy.linalg.norm(res)
        if norm == 0:
            return res
        else:
            return res / norm

    def move(self, size, lst):
        direct = self.decide_dir(lst)
        if numpy.linalg.norm(direct) == 0:
            # velocity = numpy.random.randint(-3, 4, 2, dtype=np.dtype("Float64"))
            velocity = numpy.random.rand(2) * 7 - 4
        else:
            velocity = direct
        self.pos += velocity
        self.pos = numpy.clip(self.pos, Animal.r, size - Animal.r)
        # self.pos += numpy.random.randint(-3, 4, 2)

class Rat(Animal):
    def __init__(self):
        super(Rat, self).__init__()
        self.limit = 2
        Rat.color = (0, 255, 0)
    
    def display(self, screen):
        pygame.draw.circle(screen, Rat.color, [int(self.pos[0]), int(self.pos[1])], Animal.r)

    def decide_dir(self, lst):
        res = numpy.zeros(2)
        for animal in lst:
            offset = self.pos - animal.pos
            norm = numpy.linalg.norm(offset)
            if norm < Cat.visible and norm != 0:
                res += offset / norm
        norm = numpy.linalg.norm(res) * -1
        if norm == 0:
            return res
        else:
            return res / norm

    def move(self, size, lst):
        direct = self.decide_dir(lst)
        if numpy.linalg.norm(direct) == 0:
            # velocity = numpy.random.randint(-3, 4, 2, dtype=np.dtype("Float64"))
            velocity = numpy.random.rand(2) * 7 - 4
        else:
            velocity = direct
        self.pos += velocity
        self.pos = numpy.clip(self.pos, Animal.r, size - Animal.r)

class Field(object):
    def __init__(self):
        self.rats = []
        self.cats = []
        
        self.size = 400
        pygame.init()
        self.disp_size = (self.size, self.size)
        self.screen = pygame.display.set_mode(self.disp_size)
        pygame.display.set_caption("Experiment")

    def add_cat(self, ani):
        self.cats.append(ani)
    
    def add_rat(self, ani):
        self.rats.append(ani)

    def add_age(self):
        for c in self.cats:
            c.add_age()
        for r in self.rats:
            r.add_age()

    def delete_dead(self):
       self.cats = [animal for animal in self.cats if animal.age >= 0] 
       self.rats = [animal for animal in self.rats if animal.age >= 0] 

    def print_age(self):
        for animal in self.cats:
            print animal.get_age()
        for animal in self.rats:
            print animal.get_age()

    def display(self):
        for animal in self.cats:
            animal.display(self.screen)
            animal.move(self.size, self.rats)
        for animal in self.rats:
            animal.display(self.screen)
            animal.move(self.size, self.cats)
    

field = Field()

for i in range(100):
    animal = Cat()
    animal.set_pos(numpy.random.rand(2) * (field.size - Animal.r * 2) + Animal.r)
    field.add_cat(animal)
    animal = Rat()
    animal.set_pos(numpy.random.rand(2) * (field.size - Animal.r * 2) + Animal.r)
    field.add_rat(animal)

done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    field.screen.fill((255, 255, 255))
    field.display()
    pygame.display.flip()
# field.display()
pygame.quit()

"""
for i in range(4):
     field.add_age()
field.print_age()
print(len(field.rats))
field.delete_dead()
print(len(field.rats))
"""
