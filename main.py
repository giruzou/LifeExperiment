import pygame
from pygame.locals import *
import sys
import numpy

class Animal(object):
    def __init__(self):
        Animal.r = 5

    def set_pos(self, new_pos):
        self.pos = new_pos

    def get_pos(self):
        return self.pos


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.limit = 10
        Cat.color = (255, 0, 0)
        self.visible = 60
        self.speed = 3
        self.velocity = numpy.random.rand(2) * (self.speed * 2 + 1) - self.speed - 1

    def display(self, screen):
       pygame.draw.circle(screen, Cat.color, [int(self.pos[0]), int(self.pos[1])], Animal.r)
    
    def trying_catch(self, animal):
        return None

    def decide_dir(self, lst):
        res = numpy.zeros(2)
        for animal in lst:
            offset = self.pos - animal.pos
            norm = numpy.linalg.norm(offset)
            if norm == 0:
                continue
            if norm < self.r:
                self.trying_catch(animal)
            elif norm < self.visible:
                res += offset / norm
        norm = numpy.linalg.norm(res)
        if norm == 0:
            return res
        else:
            return res / (norm * -1) * self.speed

    def move(self, size, lst):
        direct = self.decide_dir(lst)
        if numpy.linalg.norm(direct) != 0:
            self.velocity = direct
        self.pos += self.velocity

        for i in range(self.pos.size):
            if self.pos[i] > size - Animal.r:
                self.pos[i] = size - Animal.r
                self.velocity[i] *= -1
            elif self.pos[i] < Animal.r:
                self.pos[i] = Animal.r
                self.velocity[i] *= -1
        # self.pos = numpy.clip(self.pos, Animal.r, size - Animal.r)

class Rat(Animal):
    def __init__(self):
        super(Rat, self).__init__()
        self.limit = 2
        Rat.color = (0, 255, 0)
        self.visible = 60
        self.speed = 5
        self.velocity = numpy.random.rand(2) * (self.speed * 2 + 1) - self.speed - 1
    
    def display(self, screen):
        pygame.draw.circle(screen, Rat.color, [int(self.pos[0]), int(self.pos[1])], Animal.r)

    def decide_dir(self, lst):
        res = numpy.zeros(2)
        for animal in lst:
            offset = self.pos - animal.pos
            norm = numpy.linalg.norm(offset)
            if norm < self.visible and norm != 0:
                res += offset / norm
        norm = numpy.linalg.norm(res)
        if norm == 0:
            return res
        else:
            return res / norm * self.speed

    def move(self, size, lst):
        direct = self.decide_dir(lst)
        if numpy.linalg.norm(direct) != 0:
            self.velocity = direct
        self.pos += self.velocity

        for i in range(self.pos.size):
            if self.pos[i] > size - Animal.r:
                self.pos[i] = size - Animal.r
                self.velocity[i] *= -1
            elif self.pos[i] < Animal.r:
                self.pos[i] = Animal.r
                self.velocity[i] *= -1

"""
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

    def display(self):
        for animal in self.cats:
            animal.display(self.screen)
            animal.move(self.size, self.rats)
        for animal in self.rats:
            animal.display(self.screen)
            animal.move(self.size, self.cats)
    
"""

def display():
    for animal in cats:
        animal.display(screen)
        animal.move(size, rats)
    for animal in rats:
        animal.display(screen)
        animal.move(size, cats)

size = 500
screen = pygame.display.set_mode((size, size))
cats = []
rats = []

for i in range(10):
    animal = Cat()
    animal.set_pos(numpy.random.rand(2) * (size - Animal.r * 2) + Animal.r)
    cats.append(animal)
    # field.add_cat(animal)

for i in range(1):
    animal = Rat()
    animal.set_pos(numpy.random.rand(2) * (size - Animal.r * 2) + Animal.r)
    rats.append(animal)
    # field.add_rat(animal)

done = False
clock = pygame.time.Clock()
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    display()
    pygame.display.flip()
pygame.quit()



# field = Field()

"""
for i in range(10):
    animal = Cat()
    animal.set_pos(numpy.random.rand(2) * (field.size - Animal.r * 2) + Animal.r)
    field.add_cat(animal)

for i in range(1):
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
pygame.quit()

"""
"""
print(len(field.rats))
field.delete_dead()
print(len(field.rats))
"""
