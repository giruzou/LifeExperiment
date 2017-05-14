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

    def move(self, size, lst):
        direct = self.decide_dir(lst)
        if numpy.linalg.norm(direct) != 0:
            self.velocity = direct
        self.pos += self.velocity

        for i in range(self.pos.size):
            if self.pos[i] > size:
                self.pos[i] -= size
            elif self.pos[i] < 0:
                self.pos[i] += size
    
    # return real position
    def return_offset(self, animal):
         offset = numpy.empty([2])
         for i in range(offset.size):
             down = min(animal.pos[i], self.pos[i])
             up = max(animal.pos[i], self.pos[i])
             offset[i] = min(animal.pos[i] - self.pos[i], size + down - up, key=abs)
         return offset

class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.limit = 10
        Cat.color = (255, 0, 0)
        self.visible = 60
        self.speed = 5
        self.velocity = numpy.random.rand(2) * (self.speed * 2 + 1) - self.speed - 1

    def display(self, screen):
       pygame.draw.circle(screen, Cat.color, [int(self.pos[0]), int(self.pos[1])], Animal.r)
    
    def trying_catch(self, animal):
        return None

    def decide_dir(self, lst):
        res = numpy.zeros(2)
        for animal in lst:
            offset = self.return_offset(animal)
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
            return res / norm * self.speed


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
            offset = self.return_offset(animal)
            norm = numpy.linalg.norm(offset)
            if norm < self.visible and norm != 0:
                res += offset / norm
        norm = numpy.linalg.norm(res)
        if norm == 0:
            return res
        else:
            return res / (norm * -1) * self.speed



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

for i in range(1):
    animal = Cat()
    animal.set_pos(numpy.random.rand(2) * (size - Animal.r * 2) + Animal.r)
    cats.append(animal)

for i in range(10):
    animal = Rat()
    animal.set_pos(numpy.random.rand(2) * (size - Animal.r * 2) + Animal.r)
    rats.append(animal)

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
