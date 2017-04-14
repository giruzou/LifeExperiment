import numpy as np

class Animal():
    def __init__(self):
        self.age = 0

    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_pos(self):
        return (self.x, self.y)


class Field():
    def __init__(self):
        self.animals = []

    def add(self, ani):
        self.animals.append(ani)
