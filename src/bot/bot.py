from random import randint

from src.bot.genes import Genes
from src.const.cell import CellType
from src.const.direction import rand_direction, get_direction_vector, get_direction

ROTATE_45_DEGREE_GENE = 24


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
            elif is_peek_command(current_command):
                self.peek(current_command % 8)
            elif is_lookup_command(current_command):
                self.lookup(current_command % 16)
            elif is_rotate_command(current_command):
                self.rotate(current_command % 24)
            else:
                self.genes.shift_pointer(current_command)
        self.energy -= 1

    def move(self, command):
        new_cell, new_location = self.get_new_cell_from_nell_location(command)
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
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
        elif isinstance(new_cell, Bot):
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
            self.energy += 1

    def peek(self, command):
        new_cell, peek_location = self.get_new_cell_from_nell_location(command)
        if new_cell == CellType.EMPTY:
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
        elif new_cell == CellType.FOOD:
            self.genes.put_with_point(command)
        elif new_cell == CellType.POISON:
            self.genes.put_with_point(command)
            self.world.update_cell(peek_location, CellType.FOOD)
        elif new_cell == CellType.WALL:
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
        elif isinstance(new_cell, Bot):
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
            self.energy += 1

    def lookup(self, command):
        lookup_cell, lookup_location = self.get_new_cell_from_nell_location(command)
        if lookup_cell == CellType.EMPTY:
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
        elif lookup_cell == CellType.FOOD:
            self.genes.put_with_point(8 + command)
        elif lookup_cell == CellType.POISON:
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
        elif lookup_cell == CellType.WALL:
            self.genes.put_with_point(ROTATE_45_DEGREE_GENE)
        elif isinstance(lookup_cell, Bot):
            self.genes.put_with_point(8 + command)

    def rotate(self, command):
        self.direction = get_direction(self.direction, command + 1)

    def get_new_cell_from_nell_location(self, command):
        direction_vector = get_direction_vector(self.direction, command)
        new_location = self.location.transform(direction_vector)
        new_cell = self.world.get_cell(new_location)
        return new_cell, new_location

    def is_alive(self):
        return self.energy > 0


def is_move_command(command):
    return 0 <= command <= 7


def is_peek_command(command):
    return 8 <= command <= 15


def is_lookup_command(command):
    return 16 <= command <= 23


def is_rotate_command(command):
    return 24 <= command <= 30
