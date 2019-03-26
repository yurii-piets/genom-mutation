from random import randint

from src.bot.genes import Genes
from src.const.cell import CellType
from src.const.direction import rand_direction, get_direction_vector


class Bot:

    def __init__(self, location, world):
        self.energy = randint(50, 90)
        self.genes = Genes()
        self.direction = rand_direction()
        self.location = location
        self.world = world

    def execute_commands(self):
        for i in range(10):
            current_command = self.genes.get_next()
            if is_move_command(current_command):
                self.move(current_command)
                break
        self.energy -= 1

    def move(self, command):
        direction_vector = get_direction_vector(self.direction, command)
        new_location = self.location.transform(direction_vector)
        new_cell = self.world.get_cell(new_location)
        if new_cell == CellType.EMPTY:
            self.world.put_cell(new_location, self)
            self.world.update_cell(self.location, CellType.EMPTY)
            self.location = new_location
        elif new_cell == CellType.FOOD:
            self.world.update_cell(new_location, self)
            self.world.update_cell(self.location, CellType.EMPTY)
            self.location = new_location
            self.energy += 10
        elif new_cell == CellType.POISON:
            self.energy = 0
            self.world.update_cell(self.location, CellType.EMPTY)
        elif new_cell == CellType.WALL:
            self.genes.put_with_point(2)  # rotate 45 degrees
        elif isinstance(new_cell, Bot):
            self.genes.put_with_point(2)  # rotate 45 degrees
            self.energy += 1

    def is_alive(self):
        return self.energy > 0


def is_move_command(command):
    return 0 <= command <= 7
