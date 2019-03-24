from random import randint

from src.const.config import WORLD_WIDTH, WORLD_HEIGHT


class Location:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def transform(self, transition_vector):
        return Location(self.x + transition_vector[0], self.y + transition_vector[1])

    def to_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def random_location():
    rand_x = randint(0, WORLD_WIDTH)
    rand_y = randint(0, WORLD_HEIGHT)
    return Location(rand_x, rand_y)
