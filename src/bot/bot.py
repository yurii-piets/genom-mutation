from random import randint

from src.bot.genes import Genes
from src.bot.lookup_memory import LookUpMemory
from src.const.cell import CellType
from src.const.direction import rand_direction, get_direction_vector, get_direction


class Bot:

    def __init__(self, location, world, created_epoch=0):
        self.energy = randint(50, 90)
        self.direction = rand_direction()
        self.genes = Genes()
        self.location = location
        self.world = world
        self.created_epoch = created_epoch
        self.lookup_memory = LookUpMemory()
        self.ticks = 0

    def execute_commands(self):
        for _ in range(10):
            current_command = self.genes.get_next()
            if is_move_command(current_command):
                self.move(current_command)
                break
            elif is_peek_command(current_command):
                self.peek(current_command % 8)
                break
            elif is_lookup_command(current_command):
                self.lookup(current_command % 16)
            elif is_rotate_command(current_command):
                self.rotate(current_command % 24)
            else:
                self.genes.shift_pointer(current_command)
        self.energy -= 1
        self.ticks += 1

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
            self.energy += 11
        elif new_cell == CellType.POISON:
            if not self.lookup_memory.contains(new_location):
                self.energy = 0
                self.world.update_cell(self.location, CellType.POISON)

    def peek(self, command):
        new_cell, peek_location = self.get_new_cell_from_nell_location(command)
        if new_cell == CellType.FOOD:
            self.world.update_cell(peek_location, CellType.EMPTY)
            self.energy += 11
        elif new_cell == CellType.POISON:
            self.world.update_cell(peek_location, CellType.FOOD)

    def lookup(self, command):
        lookup_cell, lookup_location = self.get_new_cell_from_nell_location(command)
        self.lookup_memory.put(lookup_location, lookup_cell)

    def rotate(self, command):
        self.direction = get_direction(self.direction, command + 1)

    def get_new_cell_from_nell_location(self, command):
        direction_vector = get_direction_vector(self.direction, command)
        new_location = self.location.transform(direction_vector)
        new_cell = self.world.get_cell(new_location)
        return new_cell, new_location

    def is_alive(self):
        return self.energy > 0

    def clone(self):
        clone = Bot(None, self.world)
        clone.genes = self.genes.clone().mutate()
        return clone


def is_move_command(command):
    return 0 <= command <= 7


def is_peek_command(command):
    return 8 <= command <= 15


def is_lookup_command(command):
    return 16 <= command <= 23


def is_rotate_command(command):
    return 24 <= command <= 30
