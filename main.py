import pygame
from pygame.locals import *
import sys
import numpy
import math
import random

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
        self.walk_speed = 2
        self.max_speed = 5
        self.velocity = numpy.random.rand(2) * (self.speed * 2 + 1) - self.speed - 1
        self.target = None
        self.dead = False

    def display(self, screen):
       pygame.draw.circle(screen, Cat.color, [int(self.pos[0]), int(self.pos[1])], Animal.r)
    
    def target_exists(self):
        if self.target != None:
            targets = [ rat for rat in rats if self.target == rat]
            if(len(targets) == 0):
                self.target = None
    
    def trying_catch(self):
        global done
        done = False
        self.target.dead = True
        self.target = None

    def decide_dir(self, lst):
        self.target_exists()
        if self.target != None:
            self.speed = self.max_speed
            offset = self.return_offset(self.target)
            if numpy.linalg.norm(offset) < self.r:
                self.trying_catch()
                dire = numpy.random.rand(2) * (self.speed * 2 + 1) - self.speed - 1
                return dire / numpy.linalg.norm(dire) * self.speed
            elif numpy.linalg.norm(offset) < self.visible:
                return offset / numpy.linalg.norm(offset) * self.speed
            else:
                self.target = None
        self.speed = self.walk_speed
        if len(lst) == 0:
            return self.velocity / numpy.linalg.norm(self.velocity) * self.speed
        lst = [ animal for animal in lst if numpy.linalg.norm(self.return_offset(animal)) < self.visible ]
        if len(lst) == 0:
            # return numpy.zeros(2)
            arg = math.atan(self.velocity[1] / self.velocity[0])
            maxarg = math.pi / 7
            arg += random.random() * (maxarg * 2) - maxarg
            if self.velocity[0] < 0:
                arg += math.pi
            dire = numpy.array([math.cos(arg), math.sin(arg)]) * self.speed

            return dire
        dist_param = lambda animal: numpy.linalg.norm(self.return_offset(animal))
        self.target = min(lst, key=dist_param)
        offset = self.return_offset(self.target)
        return offset / numpy.linalg.norm(offset) * self.speed

class Rat(Animal):
    def __init__(self):
        super(Rat, self).__init__()
        self.limit = 2
        Rat.color = (0, 255, 0)
        self.visible = 60
        self.speed = 4
        self.velocity = numpy.random.rand(2) * (self.speed * 2 + 1) - self.speed - 1
        self.dead = False
    
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

def delete_dead():
    global cats, rats
    cats = [ cat for cat in cats if not cat.dead ]
    rats = [ rat for rat in rats if not rat.dead ]

size = 500
screen = pygame.display.set_mode((size, size))
cats = []
rats = []

for i in range(10):
    animal = Cat()
    animal.set_pos(numpy.random.rand(2) * (size - Animal.r * 2) + Animal.r)
    cats.append(animal)

for i in range(100):
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
    delete_dead()
    pygame.display.flip()

pygame.quit()
